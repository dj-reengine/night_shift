"""Nightly TDHCA gap. Reads the Outlook feed and the ReEngine calendar. Writes nothing to either calendar."""

import json
import os
import urllib.request
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from nightshift.calendar_gap import compare
from nightshift.envfile import load
from nightshift.envfile import resolve
from nightshift.google_auth import get_json, post_json, service_account_token, user_access_token
from nightshift.ics_feed import busy_blocks, parse_events

CHICAGO = ZoneInfo("America/Chicago")
CALENDAR_READ = "https://www.googleapis.com/auth/calendar.readonly"
CALENDAR_WRITE = "https://www.googleapis.com/auth/calendar"


def format_span(start, end):
    """Central time as YYYY-MM-DD HH:MM:SS, for a gap someone has to act on."""
    start = start.astimezone(CHICAGO)
    end = end.astimezone(CHICAGO)
    left = start.strftime("%Y-%m-%d %H:%M:%S")
    if start.date() == end.date():
        return f"{left}–{end.strftime('%H:%M:%S')} CT"
    return f"{left}–{end.strftime('%Y-%m-%d %H:%M:%S')} CT"


def _slot(item):
    return {
        "start": item["start"].astimezone(CHICAGO).isoformat(),
        "end": item["end"].astimezone(CHICAGO).isoformat(),
        "label": format_span(item["start"], item["end"]),
        "title": item.get("title") or "",
    }


def _decode_id(raw):
    import base64
    try:
        pad = "=" * ((4 - len(raw) % 4) % 4)
        text = base64.b64decode(raw + pad).decode()
    except Exception:
        return raw
    return text if "@" in text else raw


def _fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "nightshift"})
    with urllib.request.urlopen(request, timeout=40) as response:
        return response.read().decode("utf-8", "replace")


def _google_events(access_token, calendar_id, start, end):
    import urllib.parse
    query = urllib.parse.urlencode({
        "timeMin": start.isoformat(),
        "timeMax": end.isoformat(),
        "singleEvents": "true",
        "orderBy": "startTime",
        "maxResults": "100",
    })
    quoted = urllib.parse.quote(calendar_id, safe="")
    _status, payload = get_json(
        f"https://www.googleapis.com/calendar/v3/calendars/{quoted}/events?{query}",
        access_token,
    )
    events = []
    for item in payload.get("items") or []:
        start_raw = item.get("start") or {}
        end_raw = item.get("end") or {}
        events.append({
            "title": item.get("summary") or "",
            "start": _google_when(start_raw),
            "end": _google_when(end_raw),
            "out_of_office": item.get("eventType") == "outOfOffice",
            "attendees": [{"self": bool(person.get("self"))} for person in item.get("attendees") or []],
            "calendar": "",
        })
    return [event for event in events if event["start"] and event["end"]]


def _google_when(raw):
    if raw.get("dateTime"):
        return datetime.fromisoformat(raw["dateTime"]).astimezone(CHICAGO)
    if raw.get("date"):
        return datetime.strptime(raw["date"], "%Y-%m-%d").replace(tzinfo=CHICAGO)
    return None


def _overlaps_today(event, day_start, day_end):
    return event["start"] < day_end and event["end"] > day_start


def run(root, env):
    now = datetime.now(CHICAGO)
    day_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    day_end = day_start + timedelta(days=1)
    marker = os.path.join(root, "state")
    os.makedirs(marker, exist_ok=True)
    stamp = os.path.join(marker, "calendar-" + day_start.date().isoformat())
    if os.path.exists(stamp):
        return None
    feed = _fetch(env["TDHCA_CALENDAR_ICS_URL"])
    tdhca_today = [
        block for block in busy_blocks(parse_events(feed))
        if _overlaps_today(block, day_start, day_end)
    ]
    token = service_account_token(resolve(env, "GOOGLE_SERVICE_ACCOUNT_FILE"), [CALENDAR_READ])
    reengine = _google_events(token, _decode_id(env["REENGINE_CALENDAR_ID"]), day_start, day_end)
    summit = _google_events(token, _decode_id(env["SUMMIT_CALENDAR_ID"]), day_start, day_end)
    gap = compare(tdhca_today, reengine)
    fill = [_slot(item) for item in gap["fill"]]
    add = [_slot(item) for item in gap["add"]]
    lines = []
    for event in reengine:
        lines.append("ReEngine " + (event["title"] or "Busy") + " " + format_span(event["start"], event["end"]))
    for event in summit:
        lines.append("Summit " + (event["title"] or "Busy") + " " + format_span(event["start"], event["end"]))
    for block in tdhca_today:
        lines.append("TDHCA " + block["summary"] + " " + format_span(block["start"], block["end"]))
    with open(os.path.join(root, "calendar-today.json"), "w", encoding="utf-8") as handle:
        json.dump(lines, handle)
    with open(os.path.join(root, "gaps.json"), "w", encoding="utf-8") as handle:
        json.dump({"fill": fill, "add": add}, handle, indent=2)
    fill_text = "; ".join(item["label"] for item in fill)
    add_text = "; ".join(
        item["label"] + ((" " + item["title"]) if item["title"] else "") for item in add
    )
    summary = "Today's calendars are aligned."
    affects_today = bool(fill or add)
    if fill and add:
        summary = f"Add on ReEngine: {fill_text}. Add on TDHCA: {add_text}."
    elif fill:
        summary = f"Add on ReEngine: {fill_text}."
    elif add:
        summary = f"Add on TDHCA: {add_text}."
    artifact = os.path.join(root, "artifacts", "tdhca-" + day_start.date().isoformat() + ".md")
    os.makedirs(os.path.dirname(artifact), exist_ok=True)
    with open(artifact, "w", encoding="utf-8") as handle:
        handle.write("# TDHCA calendar gap\n\n")
        handle.write(summary + "\n\n")
        for item in fill:
            handle.write(f"- Add on ReEngine {item['label']} as a private TDHCA Meeting\n")
        for item in add:
            handle.write(f"- Add on TDHCA {item['label']} {item.get('title') or ''}\n")
    with open(stamp, "w", encoding="utf-8") as handle:
        handle.write(summary + "\n")
    return {
        "id": "tdhca-" + day_start.date().isoformat(),
        "trigger_key": "tdhca-" + day_start.date().isoformat(),
        "type": "tdhca",
        "vertical": "tdhca",
        "title": "TDHCA calendar gap",
        "status": "ok",
        "summary": summary,
        "tdhca_gap_today": summary if affects_today else "",
        "artifact_paths": [artifact],
    }


def create_tdhca_meeting(env, start_iso, end_iso):
    """Create a private ReEngine event named TDHCA Meeting."""
    import urllib.parse
    calendar_id = _decode_id(env["REENGINE_CALENDAR_ID"])
    quoted = urllib.parse.quote(calendar_id, safe="")
    url = f"https://www.googleapis.com/calendar/v3/calendars/{quoted}/events"
    body = {
        "summary": "TDHCA Meeting",
        "visibility": "private",
        "start": {"dateTime": start_iso, "timeZone": "America/Chicago"},
        "end": {"dateTime": end_iso, "timeZone": "America/Chicago"},
    }
    errors = []
    try:
        token = service_account_token(resolve(env, "GOOGLE_SERVICE_ACCOUNT_FILE"), [CALENDAR_WRITE])
        return post_json(url, token, body)
    except Exception as error:
        errors.append(str(error)[:160])
    try:
        token = user_access_token(resolve(env, "REENGINE_GOOGLE_TOKEN"))
        return post_json(url, token, body)
    except Exception as error:
        errors.append(str(error)[:160])
    raise RuntimeError("Could not create the event. " + " ".join(errors))


def load_and_run(root):
    from nightshift.envfile import env_path
    path = env_path()
    env = load(path)
    env["_env_path"] = path
    return run(root, env)

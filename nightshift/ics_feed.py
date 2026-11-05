"""Read busy blocks from a calendar feed. Free does not count as busy."""

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

CHICAGO = ZoneInfo("America/Chicago")
BUSY = {"busy", "away", "tentative"}


def _unfold(text):
    lines = []
    for line in text.splitlines():
        if line.startswith((" ", "\t")) and lines:
            lines[-1] += line[1:]
        else:
            lines.append(line)
    return lines


def _parse_when(raw):
    raw = (raw or "").strip()
    if not raw:
        return None, None
    if "T" not in raw:
        start = datetime.strptime(raw[:8], "%Y%m%d").replace(tzinfo=CHICAGO)
        return start, start + timedelta(days=1)
    if raw.endswith("Z"):
        start = datetime.strptime(raw[:16], "%Y%m%dT%H%M%S").replace(tzinfo=ZoneInfo("UTC"))
        return start.astimezone(CHICAGO), None
    start = datetime.strptime(raw[:15], "%Y%m%dT%H%M%S").replace(tzinfo=CHICAGO)
    return start, None


def parse_events(text):
    events = []
    current = {}
    for line in _unfold(text):
        if line == "BEGIN:VEVENT":
            current = {}
            continue
        if line == "END:VEVENT":
            if current:
                events.append(current)
            current = {}
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        name = key.split(";", 1)[0].upper()
        if name in ("DTSTART", "DTEND", "SUMMARY"):
            current[name] = value.strip()
    parsed = []
    for event in events:
        start, all_day_end = _parse_when(event.get("DTSTART"))
        end, _ = _parse_when(event.get("DTEND"))
        if start is None:
            continue
        if end is None:
            end = all_day_end or (start + timedelta(hours=1))
        summary = (event.get("SUMMARY") or "Busy").replace("\\,", ",").strip()
        parsed.append({"start": start, "end": end, "summary": summary})
    return parsed


def busy_blocks(events):
    blocks = []
    for event in events:
        if event["summary"].lower() == "free":
            continue
        if event["summary"].lower() in BUSY or event["summary"]:
            blocks.append({"start": event["start"], "end": event["end"], "summary": event["summary"]})
    return blocks

"""Primary Tracking sheet and the transcripts folder."""

import os
import urllib.parse
from datetime import datetime, timedelta, timezone

from nightshift.envfile import resolve
from nightshift.google_auth import get_json, put_json, user_access_token

SHEETS = "https://sheets.googleapis.com/v4/spreadsheets"
DRIVE = "https://www.googleapis.com/drive/v3/files"


def _token(env):
    return user_access_token(resolve(env, "REENGINE_GOOGLE_TOKEN"))


def read_tracking(env):
    sheet_id = env["PRIMARY_TRACKING_SHEET_ID"]
    token = _token(env)
    rows = []
    start = 2
    while start < 2000:
        cells = urllib.parse.quote(f"Primary Tracking!A{start}:P{start + 199}")
        _status, payload = get_json(f"{SHEETS}/{sheet_id}/values/{cells}", token)
        values = payload.get("values") or []
        if not values:
            break
        for offset, row in enumerate(values):
            padded = list(row) + [""] * (16 - len(row))
            rows.append({
                "sheet_row": start + offset,
                "entity": padded[2],
                "title": padded[3],
                "decision": padded[7],
                "filename": padded[6],
                "extracted": padded[15],
            })
        if len(values) < 200:
            break
        start += 200
    return rows


def set_extracted(env, sheet_row, value):
    sheet_id = env["PRIMARY_TRACKING_SHEET_ID"]
    token = _token(env)
    cells = urllib.parse.quote(f"Primary Tracking!P{sheet_row}")
    put_json(
        f"{SHEETS}/{sheet_id}/values/{cells}?valueInputOption=USER_ENTERED",
        token,
        {"range": f"Primary Tracking!P{sheet_row}", "values": [[value]]},
    )


ASSIGNMENTS = ("GSL-MSD", "BHCC", "ReEngine", "Summit", "TDHCA")
FOLDER_MIME = "application/vnd.google-apps.folder"


def project_of(name):
    """Project code from the start of a transcript or folder name. Blank means skip."""
    folded = (name or "").replace("_", " ").strip()
    for code in sorted(ASSIGNMENTS, key=len, reverse=True):
        if folded.lower() == code.lower() or folded.lower().startswith(code.lower() + " "):
            return code
    return ""


def _drive_list(token, query):
    url = DRIVE + "?" + urllib.parse.urlencode({
        "q": query,
        "fields": "files(id,name,mimeType,modifiedTime)",
        "pageSize": "50",
        "supportsAllDrives": "true",
        "includeItemsFromAllDrives": "true",
        "corpora": "allDrives",
    })
    _status, payload = get_json(url, token)
    return payload.get("files") or []


def recent_transcripts(env):
    folder = env["GOOGLE_DRIVE_TRANSCRIPTS_FOLDER"]
    token = _token(env)
    since = (datetime.now(timezone.utc) - timedelta(days=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
    found = []
    for item in _drive_list(token, f"'{folder}' in parents and modifiedTime > '{since}' and trashed = false"):
        name = item.get("name") or ""
        project = project_of(name)
        mime = item.get("mimeType") or ""
        nested = []
        if mime == FOLDER_MIME and project:
            nested = _drive_list(
                token,
                f"'{item.get('id')}' in parents and modifiedTime > '{since}' and trashed = false "
                f"and mimeType != '{FOLDER_MIME}'",
            )
            for child in nested:
                found.append({
                    "id": child.get("id"),
                    "name": child.get("name") or name,
                    "project": project,
                })
        elif mime != FOLDER_MIME and project:
            found.append({"id": item.get("id"), "name": name, "project": project})
        # #region agent log
        try:
            import json as _json
            import time as _time
            with open("/Users/davidjohnson/coding_projects/night_shift/.cursor/debug-7df7ff.log", "a", encoding="utf-8") as _fh:
                _fh.write(_json.dumps({
                    "sessionId": "7df7ff", "hypothesisId": "A", "runId": "post-fix",
                    "location": "google_data.py:recent_transcripts", "message": "transcript candidate",
                    "data": {"name": name, "project": project, "mime": mime, "files": len(nested), "queued": bool(project) and mime != FOLDER_MIME or bool(nested)},
                    "timestamp": int(_time.time() * 1000),
                }) + "\n")
        except Exception:
            pass
        # #endregion
    return found


def download_text(env, file_id):
    token = _token(env)
    _status, meta = get_json(f"{DRIVE}/{file_id}?fields=mimeType,name", token)
    mime = meta.get("mimeType") or ""
    if mime == "application/vnd.google-apps.document":
        url = f"{DRIVE}/{file_id}/export?mimeType=text/plain"
    else:
        url = f"{DRIVE}/{file_id}?alt=media"
    import urllib.request
    request = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    error = ""
    raw = b""
    try:
        if mime == FOLDER_MIME:
            error = "folder"
            raise ValueError("folder")
        with urllib.request.urlopen(request, timeout=40) as response:
            raw = response.read()
    except Exception as exc:
        if not error:
            error = type(exc).__name__
        raise
    finally:
        # #region agent log
        try:
            import json as _json
            import time as _time
            sample = raw[:200]
            printable = sum(1 for byte in sample if byte in (9, 10, 13) or 32 <= byte < 127)
            with open("/Users/davidjohnson/coding_projects/night_shift/.cursor/debug-7df7ff.log", "a", encoding="utf-8") as _fh:
                _fh.write(_json.dumps({
                    "sessionId": "7df7ff", "hypothesisId": "B", "runId": "download",
                    "location": "google_data.py:download_text", "message": "transcript download",
                    "data": {
                        "mime": mime, "error": error, "bytes": len(raw),
                        "printable_ratio": round(printable / max(len(sample), 1), 2),
                        "id_len": len(file_id or ""),
                    },
                    "timestamp": int(_time.time() * 1000),
                }) + "\n")
        except Exception:
            pass
        # #endregion
    return raw.decode("utf-8", "replace")[:20000]

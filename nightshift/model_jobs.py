"""Model jobs that run on the Mac. Drafts stay clean. Solicitation files stay in the local deal folder."""

import hashlib
import os
import re
import subprocess
import urllib.request
from datetime import datetime
from zoneinfo import ZoneInfo

from nightshift.envfile import env_path, load
from nightshift.google_data import download_text, set_extracted
from nightshift.ollama_client import chat
from nightshift.textutil import draft_is_clean, sensitive_text

CHICAGO = ZoneInfo("America/Chicago")
SKILLS = (
    "lean.md",
    "six-sigma.md",
    "theory-of-constraints.md",
    "change-management.md",
    "project-management.md",
)


def _env():
    path = env_path()
    env = load(path)
    env["_env_path"] = path
    return env


def _projects_root():
    env = _env()
    raw = env.get("PROJECTS_ROOT") or os.path.expanduser("~/seafile/david projects/ReEngine_Local_Projects")
    return os.path.expanduser(raw)


def _append_project_summary(project, section, root=None):
    """Create or append the running summary. The transcript file is left where it is."""
    base = root or _projects_root()
    if not project or not os.path.isdir(base):
        return "", False
    folder = ""
    for name in os.listdir(base):
        path = os.path.join(base, name)
        if name.lower() == project.lower() and os.path.isdir(path) and not os.path.islink(path):
            folder = path
            break
    if not folder:
        return "", False
    log_path = os.path.join(folder, "night_shift.md")
    created = not os.path.isfile(log_path)
    with open(log_path, "a", encoding="utf-8") as handle:
        if created:
            handle.write(f"# {project}\n")
        handle.write(section)
    return log_path, created


def _deals_root():
    env = _env()
    raw = env.get("DEALS_ROOT") or os.path.expanduser("~/coding_projects/Proposals/deals")
    return os.path.expanduser(raw)


def _skills_dir():
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(here, "skills")


def _read_file(path, limit=6000):
    with open(path, encoding="utf-8", errors="replace") as handle:
        return handle.read(limit)


def _find_file(filename):
    root = _deals_root()
    if not filename or not os.path.isdir(root):
        return ""
    for dirpath, dirnames, files in os.walk(root):
        dirnames[:] = [name for name in dirnames if name != "drive"]
        if filename in files:
            return os.path.join(dirpath, filename)
    return ""


def _text_of(path):
    if path.lower().endswith(".pdf"):
        try:
            return subprocess.check_output(["pdftotext", "-layout", path, "-"], text=True, timeout=60)[:20000]
        except Exception:
            return ""
    return _read_file(path, 20000)


def _safe_stem(filename):
    stem = os.path.splitext(os.path.basename(filename or "solicitation"))[0]
    stem = re.sub(r"[\\/:*?\"<>|]+", "-", stem).strip() or "solicitation"
    return stem


def run_mail(job):
    payload = job.get("payload") or {}
    system = (
        "Write a reply David can send. Sign off is not required. "
        "No AI wording, no footer, no mention that you are a model. "
        "If this does not need a reply (newsletter, receipt, or FYI), answer exactly SKIP."
    )
    prompt = (
        f"Who: {payload.get('who')}\n"
        f"What is needed: {payload.get('needed')}\n"
        f"Subject: {payload.get('subject')}\n\n"
        f"Message:\n{payload.get('body')}\n\n"
        f"Voice sample from David's sent mail:\n{payload.get('voice')}\n"
    )
    if job.get("type") == "mail_reengine":
        system = system.replace("If this does not need a reply (newsletter, receipt, or FYI), answer exactly SKIP.", "This message was already marked as needing a reply.")
    result = chat(prompt, system)
    text = result["text"].strip()
    if text.upper() == "SKIP":
        return {**_base(job, result), "status": "ok", "summary": "No draft.", "draft_body": ""}
    if not draft_is_clean(text):
        text = "\n".join(line for line in text.splitlines() if draft_is_clean(line))
    subject = payload.get("subject") or "Reply"
    if subject and not subject.lower().startswith("re:"):
        subject = "Re: " + subject
    return {
        **_base(job, result),
        "status": "ok",
        "summary": "Draft is ready.",
        "draft_subject": subject,
        "draft_body": text,
        "sensitivity": sensitive_text(text) or sensitive_text(payload.get("body") or ""),
        "payload": {"account": payload.get("account") or ("summit" if job.get("type") == "mail_summit" else "reengine")},
    }


def run_qb(job):
    payload = job.get("payload") or {}
    unbilled = payload.get("unbilled") or []
    lines = [
        f"{name}: This client reached out about work, and there's no invoice on file for them yet, so you might want to bill before the work piles up."
        for name in unbilled
    ]
    prompt = (
        "Write a short note of what changed in QuickBooks overnight. "
        f"New invoice ids: {', '.join(payload.get('added_invoice_ids') or []) or 'none'}. "
        f"Invoice count: {payload.get('invoice_count')}."
    )
    result = chat(prompt, "Plain sentences. No AI wording.")
    summary = result["text"].strip()
    if lines:
        summary = summary + "\n" + "\n".join(lines)
    return {**_base(job, result), "status": "ok", "summary": summary, "unbilled": bool(lines)}


def run_extract(job):
    payload = job.get("payload") or {}
    path = _find_file(payload.get("filename") or "")
    if not path:
        return {"status": "error", "summary": "The local deal folder does not have the solicitation yet."}
    source = _text_of(path)
    prompt = (
        "Write a markdown briefing for this solicitation. Include sections titled "
        "Requirements, Deadlines, Evaluation criteria, How to submit, and Submission website. "
        "How to submit must say electronic or hard-copy. "
        "Submission website must be the URL where the proposal is submitted, or None. "
        "Confidence on a match is not a pursue-or-pass decision.\n\n"
        f"Title: {payload.get('title')}\nFile: {payload.get('filename')}\n\n{source}"
    )
    result = chat(prompt, "Plain markdown. No AI wording.")
    stem = _safe_stem(payload.get("filename"))
    target = os.path.join(os.path.dirname(path), f"night_shift_results_{stem}.md")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(result["text"].strip() + "\n")
    try:
        set_extracted(_env(), payload["sheet_row"], "done")
    except Exception:
        pass
    return {
        **_base(job, result),
        "status": "ok",
        "summary": f"Wrote night_shift_results_{stem}.md",
        "artifact_text": result["text"],
        "artifact_name": f"night_shift_results_{stem}.md",
        "local_path": target,
    }


def _specialist_prompt(name):
    """The short engagement-synopsis instruction, not the whole skill file."""
    path = os.path.join(_skills_dir(), name)
    if not os.path.isfile(path):
        return "Report at most three findings from the new material. Cite the transcript."
    text = _read_file(path, 120000)
    marker = text.find("Engagement-synopsis")
    snippet = text[marker:marker + 900] if marker >= 0 else ""
    match = re.search(r'"([^"]{40,})"', snippet)
    if match:
        return match.group(1)
    return "Report at most three findings from the new material. Cite the transcript."


def run_synopsis(job):
    payload = job.get("payload") or {}
    env = _env()
    download_error = ""
    try:
        source = download_text(env, payload.get("id"))
    except Exception as exc:
        download_error = type(exc).__name__
        source = ""
    # #region agent log
    try:
        import json as _json
        import time as _time
        skill_lengths = []
        for skill_name in SKILLS:
            skill_path = os.path.join(_skills_dir(), skill_name)
            skill_lengths.append(os.path.getsize(skill_path) if os.path.isfile(skill_path) else 0)
        with open("/Users/davidjohnson/coding_projects/night_shift/.cursor/debug-7df7ff.log", "a", encoding="utf-8") as _fh:
            _fh.write(_json.dumps({
                "sessionId": "7df7ff", "hypothesisId": "D", "runId": "synopsis",
                "location": "model_jobs.py:run_synopsis", "message": "synopsis inputs",
                "data": {
                    "name": payload.get("name") or "",
                    "project": payload.get("project") or "",
                    "source_len": len(source),
                    "source_is_filename": source == (payload.get("name") or ""),
                    "download_error": download_error,
                    "skill_bytes": skill_lengths,
                    "skill_slice": 4000,
                },
                "timestamp": int(_time.time() * 1000),
            }) + "\n")
    except Exception:
        pass
    # #endregion
    if download_error or len(source.strip()) < 80:
        return {
            "status": "error",
            "summary": "Could not read the transcript." if download_error else "The transcript file has no meeting text yet.",
            "title": payload.get("project") or payload.get("name") or "",
            "vertical": "reengine",
        }
    findings = []
    tokens_in = 0
    tokens_out = 0
    for name in SKILLS:
        result = chat(
            _specialist_prompt(name) + "\n\nNew material:\n" + source[:8000],
            "One paragraph. No AI wording. Cite the transcript.",
        )
        findings.append(f"### {name.replace('.md', '').replace('-', ' ').title()}\n\n{result['text'].strip()}")
        tokens_in += result["tokens_in"]
        tokens_out += result["tokens_out"]
    merged = chat(
        "Merge these findings into one narrative. Say whether the work moved toward the charter or drifted.\n\n"
        + "\n\n".join(findings),
        "One narrative. No AI wording.",
    )
    tokens_in += merged["tokens_in"]
    tokens_out += merged["tokens_out"]
    project = payload.get("project") or "project"
    section = (
        f"\n\n## {datetime.now(CHICAGO).date().isoformat()} · {payload.get('name')}\n\n"
        + "\n\n".join(findings)
        + "\n\n### Synthesis\n\n"
        + merged["text"].strip()
        + "\n"
    )
    log_path, created = _append_project_summary(project, section)
    # #region agent log
    try:
        import json as _json
        import time as _time
        from nightshift.envfile import resolve
        from nightshift.google_auth import get_json, user_access_token
        token = user_access_token(resolve(env, "REENGINE_GOOGLE_TOKEN"))
        file_id = payload.get("id") or ""
        _status, meta = get_json(
            f"https://www.googleapis.com/drive/v3/files/{file_id}?fields=name,parents&supportsAllDrives=true",
            token,
        )
        parents = meta.get("parents") or []
        parent_name = ""
        if parents:
            _status, parent = get_json(
                f"https://www.googleapis.com/drive/v3/files/{parents[0]}?fields=name&supportsAllDrives=true",
                token,
            )
            parent_name = parent.get("name") or ""
        with open("/Users/davidjohnson/coding_projects/night_shift/.cursor/debug-7df7ff.log", "a", encoding="utf-8") as _fh:
            _fh.write(_json.dumps({
                "sessionId": "7df7ff", "hypothesisId": "G", "runId": "post-fix",
                "location": "model_jobs.py:run_synopsis", "message": "summary written, transcript left in place",
                "data": {
                    "project": project,
                    "summary_path": log_path,
                    "created": created,
                    "summary_bytes": os.path.getsize(log_path) if log_path and os.path.isfile(log_path) else 0,
                    "transcript_name": meta.get("name") or "",
                    "transcript_parent": parent_name,
                },
                "timestamp": int(_time.time() * 1000),
            }) + "\n")
    except Exception:
        pass
    # #endregion
    if not log_path:
        return {
            "status": "error",
            "summary": "The local project folder is not there, so the summary was not written.",
            "tokens_in": tokens_in,
            "tokens_out": tokens_out,
            "artifact_text": section,
            "title": project,
            "vertical": "reengine",
        }
    drift = "drift" in merged["text"].lower()
    return {
        "status": "ok",
        "summary": merged["text"].strip()[:500],
        "tokens_in": tokens_in,
        "tokens_out": tokens_out,
        "drift": merged["text"].strip()[:240] if drift else "",
        "artifact_text": section,
        "artifact_name": project + "-" + datetime.now(CHICAGO).date().isoformat() + ".md",
        "local_path": log_path,
        "title": project,
        "vertical": "reengine",
    }


def run_hubspot(job):
    lines = (job.get("payload") or {}).get("lines") or []
    result = chat(
        "Write a one-page Summit HubSpot note: stalled deals, promised follow-ups, and anything about to slip.\n\n"
        + "\n".join(lines),
        "Plain prose. No AI wording.",
    )
    return {
        **_base(job, result),
        "status": "ok",
        "summary": result["text"].strip()[:500],
        "artifact_text": result["text"],
        "artifact_name": "hubspot-" + datetime.now(CHICAGO).date().isoformat() + ".md",
        "vertical": "summit",
    }


def watch_submissions():
    root = _deals_root()
    if not os.path.isdir(root):
        return
    for dirpath, dirnames, files in os.walk(root):
        dirnames[:] = [name for name in dirnames if name != "drive"]
        for name in files:
            if not (name.startswith("night_shift_results_") and name.endswith(".md")):
                continue
            path = os.path.join(dirpath, name)
            _watch_one(path)


def _watch_one(path):
    with open(path, encoding="utf-8", errors="replace") as handle:
        text = handle.read()
    match = re.search(r"https?://\S+", text[text.lower().find("submission website"):] if "submission website" in text.lower() else "")
    if not match:
        return
    url = match.group(0).rstrip(").,")
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "nightshift"})
        with urllib.request.urlopen(request, timeout=20) as response:
            body = response.read(4000)
    except Exception:
        return
    digest = hashlib.sha256(body).hexdigest()
    marker = path + ".watch"
    previous = ""
    if os.path.isfile(marker):
        with open(marker, encoding="utf-8") as handle:
            previous = handle.read().strip()
    if previous == digest:
        return
    if previous:
        with open(path, "a", encoding="utf-8") as handle:
            handle.write(f"\n\n## Update {datetime.now(CHICAGO).date().isoformat()}\n\nThe submission page changed.\n")
    with open(marker, "w", encoding="utf-8") as handle:
        handle.write(digest)


def run_job(job):
    kind = job.get("type")
    if kind in ("mail_reengine", "mail_summit"):
        return run_mail(job)
    if kind == "qb_note":
        return run_qb(job)
    if kind == "extract":
        return run_extract(job)
    if kind == "synopsis":
        return run_synopsis(job)
    if kind == "hubspot":
        return run_hubspot(job)
    return {"status": "error", "summary": "Unknown job " + str(kind)}


def _base(job, result):
    return {
        "tokens_in": result.get("tokens_in") or 0,
        "tokens_out": result.get("tokens_out") or 0,
        "title": job.get("title") or "",
        "vertical": job.get("vertical") or "",
        "type": job.get("type") or "",
        "trigger_key": job.get("trigger_key") or "",
    }

"""File queue. Claim is an atomic rename. The same trigger cannot be queued twice."""

import json
import os
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

PRIORITIES = ("high", "standard", "low")
CHICAGO = ZoneInfo("America/Chicago")
FEED_NAMES = {
    "mail_summit": "Email - Summit",
    "mail_reengine": "Email - ReEngine",
    "extract": "Proposal",
    "hubspot": "HubSpot",
    "qb_note": "QuickBooks",
    "synopsis": "Synopsis",
    "tdhca": "TDHCA",
}


def _now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _dirs(root):
    names = ("queue", "claimed", "results", "artifacts", "failed", "removed")
    paths = {name: os.path.join(root, name) for name in names}
    for path in paths.values():
        os.makedirs(path, exist_ok=True)
    return paths


def _read(path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def _write(path, payload):
    temporary = path + ".tmp"
    with open(temporary, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")
    os.replace(temporary, path)


def _jobs(directory):
    if not os.path.isdir(directory):
        return []
    found = []
    for name in os.listdir(directory):
        if name.endswith(".json"):
            found.append(_read(os.path.join(directory, name)))
    return found


def _known_triggers(paths):
    triggers = set()
    for folder in (paths["queue"], paths["claimed"], paths["failed"], paths["results"], paths["removed"]):
        for job in _jobs(folder):
            if job.get("trigger_key"):
                triggers.add(job["trigger_key"])
    return triggers


def enqueue(root, job):
    paths = _dirs(root)
    if job["trigger_key"] in _known_triggers(paths):
        return None
    payload = {
        "id": job["id"],
        "trigger_key": job["trigger_key"],
        "type": job["type"],
        "vertical": job.get("vertical", ""),
        "priority": job.get("priority", "standard"),
        "attempt": job.get("attempt", 1),
        "created_at": job.get("created_at") or _now(),
        "payload_path": job.get("payload_path", ""),
        "title": job.get("title", job["type"]),
        "received_at": job.get("received_at") or "",
        "run_now": bool(job.get("run_now", False)),
        "payload": job.get("payload") or {},
    }
    if payload["priority"] not in PRIORITIES:
        payload["priority"] = "standard"
    _write(os.path.join(paths["queue"], payload["id"] + ".json"), payload)
    return payload


def dismiss(root, job_id, reason):
    """Take a job off the queue and remember why, so it is not queued again."""
    reason = (reason or "").strip()
    if not reason:
        raise ValueError("reason")
    paths = _dirs(root)
    source = os.path.join(paths["queue"], job_id + ".json")
    if not os.path.exists(source):
        source = os.path.join(paths["claimed"], job_id + ".json")
    if not os.path.exists(source):
        return None
    job = _read(source)
    os.remove(source)
    job["removed_at"] = _now()
    job["removed_reason"] = reason
    _write(os.path.join(paths["removed"], job["id"] + ".json"), job)
    write_removals_log(root)
    return job


def _removal_record(job):
    payload = job.get("payload") if isinstance(job.get("payload"), dict) else {}
    when = job.get("removed_at") or ""
    try:
        parsed = datetime.fromisoformat(when)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        local = parsed.astimezone(CHICAGO).strftime("%Y-%m-%d %H:%M:%S")
    except (TypeError, ValueError):
        local = ""
    return {
        "id": job.get("id") or "",
        "removed_at": when,
        "removed_at_ct": local,
        "feed": FEED_NAMES.get(job.get("type") or "", job.get("type") or "Night Shift"),
        "title": job.get("title") or "",
        "who": payload.get("who") or "",
        "subject": payload.get("subject") or "",
        "entity": payload.get("entity") or "",
        "reason": job.get("removed_reason") or "",
    }


def write_removals_log(root):
    """One review file: what left the queue, and why. Mail bodies stay out of it."""
    jobs = _jobs(os.path.join(root, "removed"))
    jobs.sort(key=lambda job: (job.get("removed_at") or "", job.get("id") or ""))
    _write(os.path.join(root, "removals.json"), {
        "note": "What left the queue, and why. Use these reasons when deciding what to queue next.",
        "items": [_removal_record(job) for job in jobs],
    })


def set_priority(root, job_id, priority):
    if priority not in PRIORITIES:
        raise ValueError(priority)
    path = os.path.join(_dirs(root)["queue"], job_id + ".json")
    if not os.path.exists(path):
        return None
    job = _read(path)
    job["priority"] = priority
    _write(path, job)
    return job


def claim_next(root):
    paths = _dirs(root)
    now = _now()
    waiting = [job for job in _jobs(paths["queue"]) if (job.get("retry_after") or "") <= now]
    rank = {name: index for index, name in enumerate(PRIORITIES)}
    waiting.sort(key=lambda job: (rank.get(job["priority"], 1), job["created_at"], job["id"]))
    for job in waiting:
        source = os.path.join(paths["queue"], job["id"] + ".json")
        target = os.path.join(paths["claimed"], job["id"] + ".json")
        try:
            os.rename(source, target)
        except FileNotFoundError:
            continue
        job["claimed_at"] = _now()
        _write(target, job)
        return job
    return None


def release(root, job_id, **updates):
    """Put a claimed job back without counting a failure. Used when the Mac is not idle."""
    paths = _dirs(root)
    source = os.path.join(paths["claimed"], job_id + ".json")
    if not os.path.exists(source):
        return None
    job = _read(source)
    os.remove(source)
    job.pop("claimed_at", None)
    job.pop("stalled", None)
    job.update(updates)
    _write(os.path.join(paths["queue"], job_id + ".json"), job)
    return job


def fail(root, job_id):
    paths = _dirs(root)
    source = os.path.join(paths["claimed"], job_id + ".json")
    if not os.path.exists(source):
        source = os.path.join(paths["queue"], job_id + ".json")
    if not os.path.exists(source):
        return None
    job = _read(source)
    os.remove(source)
    if job.get("attempt", 1) >= 2:
        job["failed_at"] = _now()
        _write(os.path.join(paths["failed"], job["id"] + ".json"), job)
        job["outcome"] = "failed"
        return job
    job["attempt"] = 2
    job.pop("claimed_at", None)
    _write(os.path.join(paths["queue"], job["id"] + ".json"), job)
    job["outcome"] = "requeued"
    return job


def complete(root, job_id, result):
    paths = _dirs(root)
    source = os.path.join(paths["claimed"], job_id + ".json")
    if os.path.exists(source):
        claimed = _read(source)
        os.remove(source)
    else:
        claimed = {}
    result = dict(result)
    result["id"] = job_id
    result["trigger_key"] = result.get("trigger_key") or claimed.get("trigger_key", "")
    result["type"] = result.get("type") or claimed.get("type", "")
    result["vertical"] = result.get("vertical") or claimed.get("vertical", "")
    result["title"] = result.get("title") or claimed.get("title", "")
    result["priority"] = result.get("priority") or claimed.get("priority", "")
    claimed_payload = claimed.get("payload") if isinstance(claimed.get("payload"), dict) else {}
    if claimed_payload.get("entity") and not result.get("entity"):
        result["entity"] = claimed_payload["entity"]
    result["finished_at"] = result.get("finished_at") or _now()
    _write(os.path.join(paths["results"], job_id + ".json"), result)
    _add_stats(root, result)
    return result


def _add_stats(root, result):
    path = os.path.join(root, "stats.json")
    stats = {"tokens_in": 0, "tokens_out": 0, "runs": 0, "failures": 0}
    if os.path.exists(path):
        stats.update(_read(path))
    stats["tokens_in"] += int(result.get("tokens_in") or 0)
    stats["tokens_out"] += int(result.get("tokens_out") or 0)
    stats["runs"] += 1
    if result.get("status") != "ok":
        stats["failures"] += 1
    _write(path, stats)


def snapshot(root):
    paths = _dirs(root)
    stats = {"tokens_in": 0, "tokens_out": 0, "runs": 0, "failures": 0}
    stats_path = os.path.join(root, "stats.json")
    if os.path.exists(stats_path):
        stats.update(_read(stats_path))
    mac = {}
    mac_path = os.path.join(root, "mac-status.json")
    if os.path.exists(mac_path):
        mac = _read(mac_path)
    return {
        "queue": _jobs(paths["queue"]),
        "claimed": _jobs(paths["claimed"]),
        "results": _jobs(paths["results"]),
        "failed": _jobs(paths["failed"]),
        "stats": stats,
        "mac": mac,
    }

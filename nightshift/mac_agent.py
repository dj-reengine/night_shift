"""The Mac polls Proxmox over SSH. It opens no port."""

import json
import os
import subprocess
import time
from datetime import datetime, timezone

from nightshift.idle import gate
from nightshift.model_jobs import run_job, watch_submissions
from nightshift.triage import reply_rows

PROXMOX = os.environ.get("NIGHTSHIFT_PROXMOX", "root@10.0.0.97")
KEY = os.environ.get("NIGHTSHIFT_SSH_KEY", os.path.expanduser("~/.ssh/id_homelab"))
TRIAGE = os.path.expanduser(
    os.environ.get(
        "NIGHTSHIFT_TRIAGE",
        "~/Documents/ReEngine/Email Triage/reengine-email-triage.md",
    )
)
SPOOL = os.path.expanduser("~/Library/Application Support/Night Shift")


def _ssh(remote_argv, input_text=""):
    command = [
        "ssh", "-i", KEY, "-o", "IdentitiesOnly=yes", "-o", "ConnectTimeout=20",
        PROXMOX,
        "pct exec 127 -- env PYTHONPATH=/opt NIGHTSHIFT_ROOT=/var/lib/night-shift "
        "NIGHTSHIFT_ENV=/var/lib/night-shift/secrets/night-shift.env "
        "python3 -m nightshift.remote " + " ".join(remote_argv),
    ]
    completed = subprocess.run(command, input=input_text, text=True, capture_output=True, timeout=180)
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or completed.stdout.strip() or "ssh failed")
    return completed.stdout.strip()


def _push_json(command, payload):
    path = os.path.join(SPOOL, "outbox", "push.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle)
    remote = "/tmp/nightshift-push.json"
    subprocess.run(
        ["scp", "-i", KEY, "-o", "IdentitiesOnly=yes", path, f"{PROXMOX}:{remote}"],
        check=True, capture_output=True, text=True, timeout=60,
    )
    subprocess.run(
        ["ssh", "-i", KEY, "-o", "IdentitiesOnly=yes", PROXMOX, f"pct push 127 {remote} {remote}"],
        check=True, capture_output=True, text=True, timeout=60,
    )
    return _ssh([command, remote])


def _sensors():
    battery = subprocess.check_output(["pmset", "-g", "batt"], text=True)
    on_ac = "AC Power" in battery
    idle = 0
    try:
        raw = subprocess.check_output(["ioreg", "-c", "IOHIDSystem"], text=True)
        for line in raw.splitlines():
            if "HIDIdleTime" in line:
                idle = int(line.split("=")[-1].strip()) / 1_000_000_000
                break
    except Exception:
        idle = 0
    cpu = 0.0
    try:
        raw = subprocess.check_output(["ps", "-A", "-o", "%cpu="], text=True)
        total = sum(float(item) for item in raw.split() if item.replace(".", "", 1).isdigit())
        cpu = total / max(os.cpu_count() or 1, 1)
    except Exception:
        cpu = 0.0
    return on_ac, idle, cpu


def _status(utilization, active=""):
    payload = {
        "seen_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "utilization": utilization,
        "active_job": active,
        "progress_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
    }
    try:
        _push_json("status", payload)
    except Exception:
        pass


def _enqueue_reengine():
    if not os.path.isfile(TRIAGE):
        return
    with open(TRIAGE, encoding="utf-8") as handle:
        rows = reply_rows(handle.read())
    for row in rows:
        row["account"] = "reengine"
        try:
            _push_json("enqueue-mail", row)
        except Exception:
            continue


def _hold_awake(proc, on_ac, now, running):
    from nightshift.idle import is_overnight
    want = on_ac and (is_overnight(now) or running)
    if want and proc is None:
        return subprocess.Popen(["caffeinate", "-ims"])
    if not want and proc is not None:
        proc.terminate()
        return None
    return proc


def once(now=None):
    now = now or datetime.now().astimezone()
    os.makedirs(os.path.join(SPOOL, "incoming"), exist_ok=True)
    os.makedirs(os.path.join(SPOOL, "work"), exist_ok=True)
    os.makedirs(os.path.join(SPOOL, "outbox"), exist_ok=True)
    on_ac, idle, cpu = _sensors()
    decision = gate(on_ac, idle, cpu, now)
    utilization = {"start": "working", "battery": "on battery", "in use": "in use", "busy": "in use"}[decision]
    _status(utilization)
    try:
        watch_submissions()
    except Exception:
        pass
    try:
        _enqueue_reengine()
    except Exception:
        pass
    raw = _ssh(["claim"])
    job = json.loads(raw or "{}")
    if not job:
        return decision
    if decision == "battery" or (decision != "start" and not job.get("run_now")):
        _push_json("release", {"id": job["id"]})
        return decision
    _status("working", job.get("id") or "")
    work = os.path.join(SPOOL, "work", job["id"] + ".json")
    with open(work, "w", encoding="utf-8") as handle:
        json.dump(job, handle)
    try:
        result = run_job(job)
    except Exception as error:
        result = {"status": "error", "summary": type(error).__name__}
    result["id"] = job["id"]
    _push_json("complete", result)
    return "done"


def main():
    awake = None
    while True:
        started = time.time()
        try:
            outcome = once()
        except Exception:
            outcome = "error"
        delay = 120 if outcome in ("start", "done") else 600
        awake = _hold_awake(awake, outcome != "battery", datetime.now().astimezone(), outcome == "done")
        time.sleep(max(1, delay - (time.time() - started)))


if __name__ == "__main__":
    main()

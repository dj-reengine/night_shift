"""Commands the container runs for the Mac: claim, complete, enqueue, dispatch."""

import json
import os
import sys

from nightshift.dispatcher import dispatch, enqueue_mail, finish_mail
from nightshift.envfile import env_path, load
from nightshift.queue import claim_next, complete, fail, release


def _root():
    return os.environ.get("NIGHTSHIFT_ROOT", "/var/lib/night-shift")


def _read_input(path):
    if path:
        with open(path, encoding="utf-8") as handle:
            return json.load(handle)
    return json.load(sys.stdin)


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    command = argv[0] if argv else ""
    root = _root()
    if command == "dispatch":
        print(json.dumps(dispatch(root)))
        return 0
    if command == "claim":
        job = claim_next(root)
        print(json.dumps(job or {}))
        return 0
    if command == "enqueue-mail":
        row = _read_input(argv[1] if len(argv) > 1 else "")
        env = load(env_path())
        env["_env_path"] = env_path()
        job = enqueue_mail(root, env, row.get("account") or "reengine", row)
        print(json.dumps({"id": job["id"] if job else ""}))
        return 0
    if command == "complete":
        result = _read_input(argv[1] if len(argv) > 1 else "")
        env = load(env_path())
        if result.get("draft_body"):
            try:
                finish_mail(env, result)
            except Exception as error:
                fail(root, result.get("id") or "")
                print(json.dumps({"status": "error", "summary": type(error).__name__}))
                return 1
        if result.get("artifact_text") and result.get("artifact_name"):
            directory = os.path.join(root, "artifacts")
            os.makedirs(directory, exist_ok=True)
            artifact = os.path.join(directory, os.path.basename(result["artifact_name"]))
            with open(artifact, "w", encoding="utf-8") as handle:
                handle.write(result["artifact_text"])
            result["artifact_paths"] = [artifact]
        if result.get("status") == "error" and "deal folder" in (result.get("summary") or ""):
            from datetime import datetime, timedelta, timezone
            later = (datetime.now(timezone.utc) + timedelta(minutes=30)).replace(microsecond=0).isoformat()
            release(root, result.get("id") or "", retry_after=later)
            print(json.dumps({"outcome": "waiting"}))
            return 0
        if result.get("status") == "error":
            outcome = fail(root, result.get("id") or "")
            print(json.dumps({"outcome": (outcome or {}).get("outcome")}))
            return 0
        stored = complete(root, result.get("id") or "", result)
        print(json.dumps({"status": stored.get("status")}))
        return 0
    if command == "release":
        payload = _read_input(argv[1] if len(argv) > 1 else "")
        release(root, payload.get("id") or "")
        print(json.dumps({"outcome": "released"}))
        return 0
    if command == "status":
        payload = _read_input(argv[1] if len(argv) > 1 else "")
        path = os.path.join(root, "mac-status.json")
        with open(path, "w", encoding="utf-8") as handle:
            json.dump(payload, handle)
        print("ok")
        return 0
    print("usage: remote dispatch|claim|enqueue-mail|complete|status")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

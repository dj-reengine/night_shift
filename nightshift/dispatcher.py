"""One pass of the Proxmox jobs that do not need the Mac, plus the queue for the ones that do."""

import email
import email.utils
import hashlib
import imaplib
import json
import os
import re
import urllib.request
from datetime import datetime, timedelta, timezone
from email.header import decode_header
from zoneinfo import ZoneInfo

from nightshift import qbo
from nightshift.calendar_job import run as calendar_run
from nightshift.envfile import env_path, load
from nightshift.google_data import read_tracking, recent_transcripts, set_extracted
from nightshift.mail_writer import append_draft
from nightshift.queue import complete, dismiss, enqueue, fail, snapshot

CHICAGO = ZoneInfo("America/Chicago")


def _env():
    path = env_path()
    env = load(path)
    env["_env_path"] = path
    return env, path


def _imap(env, user_key, password_key):
    client = imaplib.IMAP4_SSL(env.get("IMAP_HOST") or "imap.gmail.com", 993, timeout=30)
    client.login(env[user_key], env[password_key].replace(" ", ""))
    return client


_AUTOMATED_ADDRESS = re.compile(r"(no[\W_]*reply|do[\W_]*not[\W_]*reply|notifications?)", re.I)
_CODE_SUBJECT = re.compile(r"\b(log[\s-]?in code|verification code|security code|one-time (password|code))\b", re.I)


def _received_at(value):
    if not value:
        return ""
    try:
        parsed = email.utils.parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return ""
    if parsed is None:
        return ""
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=CHICAGO)
    return parsed.astimezone(timezone.utc).replace(microsecond=0).isoformat()


def mail_is_noise(who, subject="", headers=None, account_address=""):
    """True for no-reply mail, bulk mail, and mail that is not addressed to the mailbox."""
    headers = headers or {}
    _name, address = email.utils.parseaddr(who or "")
    local = address.split("@", 1)[0].lower()
    if _AUTOMATED_ADDRESS.search(address or ""):
        return True
    if local.endswith("orders"):
        return True
    if _CODE_SUBJECT.search(subject or ""):
        return True
    precedence = (headers.get("Precedence") or "").strip().lower()
    if precedence in ("bulk", "list", "junk"):
        return True
    if headers.get("List-Unsubscribe") or headers.get("List-Id"):
        return True
    directed = " ".join(headers.get(key) or "" for key in ("To", "Cc")).strip()
    if account_address and directed and account_address.lower() not in directed.lower():
        return True
    return False


def reply_settled_reason(who, to, cc, account_address):
    """Why this thread is finished, or empty when the latest message still needs David."""
    _name, sender = email.utils.parseaddr(who or "")
    me = (account_address or "").lower()
    if me and sender.lower() == me:
        return "Already answered this thread"
    directed = f"{to or ''} {cc or ''}"
    if me and me not in directed.lower():
        return "The latest reply is not to me"
    return ""


def _parse_thrid(fetched):
    chunks = []

    def walk(value):
        if isinstance(value, bytes):
            chunks.append(value)
        elif isinstance(value, (tuple, list)):
            for item in value:
                walk(item)

    walk(fetched)
    match = re.search(br"X-GM-THRID (\d+)", b" ".join(chunks))
    return match.group(1).decode() if match else ""


def _decode(value):
    if not value:
        return ""
    parts = []
    for text, encoding in decode_header(value):
        if isinstance(text, bytes):
            parts.append(text.decode(encoding or "utf-8", "replace"))
        else:
            parts.append(text)
    return "".join(parts)


def _body(raw):
    message = email.message_from_bytes(raw)
    chunks = []
    if message.is_multipart():
        for part in message.walk():
            if part.get_content_type() == "text/plain" and "attachment" not in str(part.get("Content-Disposition")):
                payload = part.get_payload(decode=True) or b""
                chunks.append(payload.decode(part.get_content_charset() or "utf-8", "replace"))
    else:
        payload = message.get_payload(decode=True) or b""
        chunks.append(payload.decode(message.get_content_charset() or "utf-8", "replace"))
    return "\n".join(chunks)[:6000]


def recent_sender_names(env):
    names = []
    since = (datetime.now(CHICAGO) - timedelta(days=2)).strftime("%d-%b-%Y")
    for user_key, password_key in (
        ("REENGINE_IMAP_USER", "REENGINE_IMAP_APP_PASSWORD"),
        ("SUMMIT_IMAP_USER", "SUMMIT_IMAP_APP_PASSWORD"),
    ):
        if not env.get(password_key):
            continue
        client = _imap(env, user_key, password_key)
        try:
            client.select("INBOX", readonly=True)
            status, data = client.search(None, "SINCE", since)
            ids = data[0].split()[-20:] if status == "OK" and data and data[0] else []
            for number in ids:
                fetched = client.fetch(number, "(BODY.PEEK[HEADER.FIELDS (FROM)])")
                raw = fetched[1][0][1] if fetched[1] and isinstance(fetched[1][0], tuple) else b""
                name, address = email.utils.parseaddr(_decode(raw.split(b":", 1)[-1].decode("utf-8", "replace")))
                names.append(name or address)
        finally:
            client.logout()
    return names


def fetch_message(env, user_key, password_key, message_id):
    client = _imap(env, user_key, password_key)
    try:
        client.select("INBOX", readonly=True)
        header = message_id.strip().strip("<>")
        status, data = client.search(None, "HEADER", "Message-ID", f"<{header}>")
        ids = data[0].split() if status == "OK" and data and data[0] else []
        if not ids:
            status, data = client.search(None, "X-GM-THRID", message_id)
            ids = data[0].split() if status == "OK" and data and data[0] else []
        if not ids:
            return {}
        fetched = client.fetch(ids[-1], "(BODY.PEEK[])")
        raw = fetched[1][0][1] if fetched[1] and isinstance(fetched[1][0], tuple) else b""
        message = email.message_from_bytes(raw)
        return {"subject": _decode(message.get("Subject")), "body": _body(raw), "from": _decode(message.get("From"))}
    finally:
        client.logout()


def voice_sample(env, user_key, password_key):
    client = _imap(env, user_key, password_key)
    try:
        client.select('"[Gmail]/Sent Mail"', readonly=True)
        status, data = client.search(None, "ALL")
        ids = data[0].split()[-2:] if status == "OK" and data and data[0] else []
        samples = []
        for number in ids:
            fetched = client.fetch(number, "(BODY.PEEK[])")
            raw = fetched[1][0][1] if fetched[1] and isinstance(fetched[1][0], tuple) else b""
            samples.append(_body(raw)[:800])
        return "\n\n".join(samples)
    finally:
        client.logout()


def _header_from_fetch(fetched):
    if not fetched or not fetched[1]:
        return b""
    part = fetched[1][0]
    if isinstance(part, tuple) and len(part) > 1 and isinstance(part[1], bytes):
        return part[1]
    return b""


def _latest_header(client, thrid):
    status, data = client.search(None, "X-GM-THRID", thrid)
    ids = data[0].split() if status == "OK" and data and data[0] else []
    latest = None
    latest_stamp = ""
    for number in ids:
        fetched = client.fetch(number, "(BODY.PEEK[HEADER.FIELDS (FROM TO CC DATE)])")
        header = email.message_from_bytes(_header_from_fetch(fetched))
        stamp = _received_at(header.get("Date"))
        if latest is None or stamp >= latest_stamp:
            latest = header
            latest_stamp = stamp
    return latest


def thread_settled_reason(env, account, message_id):
    """Empty when the latest message in the thread still needs a reply from this mailbox."""
    if account == "reengine":
        user_key, password_key = "REENGINE_IMAP_USER", "REENGINE_IMAP_APP_PASSWORD"
    else:
        user_key, password_key = "SUMMIT_IMAP_USER", "SUMMIT_IMAP_APP_PASSWORD"
    address = env.get(user_key) or ""
    header_id = (message_id or "").strip().strip("<>")
    if not header_id or not address or not env.get(password_key):
        return ""
    client = _imap(env, user_key, password_key)
    try:
        client.select('"[Gmail]/All Mail"', readonly=True)
        status, data = client.search(None, "HEADER", "Message-ID", f"<{header_id}>")
        ids = data[0].split() if status == "OK" and data and data[0] else []
        if not ids:
            return ""
        thrid = _parse_thrid(client.fetch(ids[-1], "(X-GM-THRID)"))
        if not thrid:
            return ""
        latest = _latest_header(client, thrid)
        if latest is None:
            return ""
        return reply_settled_reason(
            _decode(latest.get("From")),
            _decode(latest.get("To")),
            _decode(latest.get("Cc")),
            address,
        )
    finally:
        client.logout()


def _job_id(key):
    return hashlib.sha256(key.encode()).hexdigest()[:16]


def enqueue_mail(root, env, account, row):
    if account == "reengine":
        user_key, password_key, vertical = "REENGINE_IMAP_USER", "REENGINE_IMAP_APP_PASSWORD", "reengine"
    else:
        user_key, password_key, vertical = "SUMMIT_IMAP_USER", "SUMMIT_IMAP_APP_PASSWORD", "summit"
    trigger = f"{account}:{row.get('thread_id')}:{row.get('message_id')}"
    try:
        if thread_settled_reason(env, account, row.get("message_id") or ""):
            return None
    except Exception:
        pass
    message = {}
    try:
        message = fetch_message(env, user_key, password_key, row.get("message_id") or "")
    except Exception as error:
        message = {"subject": row.get("who") or "Reply", "body": "", "error": type(error).__name__}
    sample = ""
    try:
        sample = voice_sample(env, user_key, password_key)
    except Exception:
        sample = ""
    return enqueue(root, {
        "id": _job_id(trigger),
        "trigger_key": trigger,
        "type": "mail_" + account,
        "vertical": vertical,
        "title": row.get("who") or message.get("subject") or "Mail",
        "payload": {
            "who": row.get("who") or "",
            "needed": row.get("needed") or "",
            "subject": message.get("subject") or row.get("who") or "Reply",
            "body": message.get("body") or row.get("needed") or "",
            "voice": sample,
            "account": account,
        },
    })


def _header_fields(header):
    return {
        "To": _decode(header.get("To")),
        "Cc": _decode(header.get("Cc")),
        "Precedence": _decode(header.get("Precedence")),
        "List-Unsubscribe": "yes" if header.get("List-Unsubscribe") else "",
        "List-Id": "yes" if header.get("List-Id") else "",
    }


def _summit_messages(env):
    account = env.get("SUMMIT_IMAP_USER") or ""
    client = None
    threads = None
    found = []
    try:
        client = _imap(env, "SUMMIT_IMAP_USER", "SUMMIT_IMAP_APP_PASSWORD")
        try:
            threads = _imap(env, "SUMMIT_IMAP_USER", "SUMMIT_IMAP_APP_PASSWORD")
            threads.select('"[Gmail]/All Mail"', readonly=True)
        except Exception:
            threads = None
        client.select("INBOX", readonly=True)
        since = (datetime.now(CHICAGO) - timedelta(days=2)).strftime("%d-%b-%Y")
        status, data = client.search(None, "SINCE", since)
        ids = data[0].split()[-40:] if status == "OK" and data and data[0] else []
        fields = "(X-GM-THRID BODY.PEEK[HEADER.FIELDS (MESSAGE-ID SUBJECT FROM DATE TO CC PRECEDENCE LIST-UNSUBSCRIBE LIST-ID)])"
        for number in reversed(ids):
            fetched = client.fetch(number, fields)
            header = email.message_from_bytes(_header_from_fetch(fetched))
            who = _decode(header.get("From"))
            subject = _decode(header.get("Subject"))
            mail_headers = _header_fields(header)
            if mail_is_noise(who, subject, mail_headers, account):
                continue
            message_id = (header.get("Message-ID") or "").strip()
            if not message_id:
                continue
            thrid = _parse_thrid(fetched)
            if threads and thrid:
                try:
                    latest = _latest_header(threads, thrid)
                except Exception:
                    latest = None
                if latest is not None and reply_settled_reason(
                    _decode(latest.get("From")),
                    _decode(latest.get("To")),
                    _decode(latest.get("Cc")),
                    account,
                ):
                    continue
            full = client.fetch(number, "(BODY.PEEK[])")
            full_raw = full[1][0][1] if full[1] and isinstance(full[1][0], tuple) else b""
            found.append({
                "message_id": message_id,
                "thread_id": thrid or message_id,
                "who": who,
                "needed": subject,
                "subject": subject,
                "received_at": _received_at(header.get("Date")),
                "headers": mail_headers,
                "body": _body(full_raw),
            })
            if len(found) >= 8:
                break
        found.reverse()
    finally:
        if client:
            client.logout()
        if threads:
            threads.logout()
    return found


def _message_received_at(env, account, message_id):
    if account == "reengine":
        user_key, password_key = "REENGINE_IMAP_USER", "REENGINE_IMAP_APP_PASSWORD"
    else:
        user_key, password_key = "SUMMIT_IMAP_USER", "SUMMIT_IMAP_APP_PASSWORD"
    header_id = (message_id or "").strip().strip("<>")
    if not header_id or not env.get(password_key):
        return ""
    client = _imap(env, user_key, password_key)
    try:
        for mailbox in ("INBOX", '"[Gmail]/All Mail"'):
            client.select(mailbox, readonly=True)
            status, data = client.search(None, "HEADER", "Message-ID", f"<{header_id}>")
            ids = data[0].split() if status == "OK" and data and data[0] else []
            if not ids:
                continue
            fetched = client.fetch(ids[-1], "(BODY.PEEK[HEADER.FIELDS (DATE)])")
            raw = fetched[1][0][1] if fetched[1] and isinstance(fetched[1][0], tuple) else b""
            return _received_at(email.message_from_bytes(raw).get("Date"))
    finally:
        client.logout()
    return ""


def prune_queued_mail(root, env):
    """Drop queued no-reply and blast mail, and record the real sent time on the rest."""
    directory = os.path.join(root, "queue")
    if not os.path.isdir(directory):
        return 0
    removed = 0
    for name in list(os.listdir(directory)):
        if not name.endswith(".json"):
            continue
        path = os.path.join(directory, name)
        with open(path, encoding="utf-8") as handle:
            job = json.load(handle)
        if not str(job.get("type") or "").startswith("mail"):
            continue
        payload = job.get("payload") if isinstance(job.get("payload"), dict) else {}
        account = "summit" if "summit" in (job.get("type") or "") else "reengine"
        address = env.get("SUMMIT_IMAP_USER") if account == "summit" else env.get("REENGINE_IMAP_USER")
        if mail_is_noise(payload.get("who") or job.get("title") or "", payload.get("subject") or "", payload.get("headers") or {}, address or ""):
            dismiss(root, job["id"], "No-reply or bulk mail")
            removed += 1
            continue
        try:
            settled = thread_settled_reason(env, account, payload.get("message_id") or "")
        except Exception:
            settled = ""
        if settled:
            dismiss(root, job["id"], settled)
            removed += 1
            continue
        if job.get("received_at") or payload.get("received_at"):
            continue
        try:
            when = _message_received_at(env, account, payload.get("message_id") or "")
        except Exception:
            when = ""
        if not when:
            continue
        payload["received_at"] = when
        job["payload"] = payload
        job["received_at"] = when
        temporary = path + ".tmp"
        with open(temporary, "w", encoding="utf-8") as handle:
            json.dump(job, handle, indent=2)
            handle.write("\n")
        os.replace(temporary, path)
    return removed


def _proposals(root, env):
    rows = read_tracking(env)
    queued = []
    for row in rows:
        if row["decision"].strip().lower() != "pursue":
            continue
        if row["extracted"].strip().lower() == "done":
            continue
        if not row["filename"]:
            continue
        trigger = "extract:" + row["filename"]
        job = enqueue(root, {
            "id": _job_id(trigger),
            "trigger_key": trigger,
            "type": "extract",
            "vertical": "reengine",
            "title": row["title"] or row["filename"],
            "payload": row,
        })
        if job and row["extracted"].strip().lower() != "queued":
            set_extracted(env, row["sheet_row"], "queued")
            queued.append(job["id"])
    return queued


def stamp_proposal_entities(root, env):
    """Fill entity onto proposal jobs that were queued before that field existed."""
    by_file = {row["filename"]: row for row in read_tracking(env) if row.get("filename")}
    updated = 0
    for folder in ("queue", "claimed"):
        directory = os.path.join(root, folder)
        if not os.path.isdir(directory):
            continue
        for name in os.listdir(directory):
            if not name.endswith(".json"):
                continue
            path = os.path.join(directory, name)
            with open(path, encoding="utf-8") as handle:
                job = json.load(handle)
            if job.get("type") != "extract":
                continue
            payload = job.get("payload") if isinstance(job.get("payload"), dict) else {}
            row = by_file.get(payload.get("filename") or "")
            entity = (row or {}).get("entity") or ""
            if not entity or payload.get("entity") == entity:
                continue
            payload["entity"] = entity
            job["payload"] = payload
            temporary = path + ".tmp"
            with open(temporary, "w", encoding="utf-8") as handle:
                json.dump(job, handle, indent=2)
                handle.write("\n")
            os.replace(temporary, path)
            updated += 1
    return updated


def _transcripts(root, env):
    added = []
    for item in recent_transcripts(env):
        trigger = "synopsis:" + item["name"]
        job = enqueue(root, {
            "id": _job_id(trigger),
            "trigger_key": trigger,
            "type": "synopsis",
            "vertical": "reengine",
            "title": item["project"],
            "payload": item,
        })
        if job:
            added.append(job["id"])
    return added


def _hubspot(root, env):
    today = datetime.now(CHICAGO)
    if today.weekday() != 6:
        return None
    marker = os.path.join(root, "state", "hubspot-" + today.date().isoformat())
    if os.path.exists(marker):
        return None
    request = urllib.request.Request(
        "https://api.hubapi.com/crm/v3/objects/deals?limit=20&properties=dealname,dealstage,notes_last_updated",
        headers={"Authorization": f"Bearer {env['SUMMIT_HUBSPOT_ACCESS_TOKEN']}"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.loads(response.read().decode())
    lines = []
    for deal in payload.get("results") or []:
        props = deal.get("properties") or {}
        lines.append(f"{props.get('dealname') or 'Deal'} · {props.get('dealstage') or ''}")
    os.makedirs(os.path.dirname(marker), exist_ok=True)
    with open(marker, "w", encoding="utf-8") as handle:
        handle.write("queued\n")
    return enqueue(root, {
        "id": _job_id("hubspot-" + today.date().isoformat()),
        "trigger_key": "hubspot-" + today.date().isoformat(),
        "type": "hubspot",
        "vertical": "summit",
        "title": "Summit HubSpot digest",
        "payload": {"lines": lines},
    })


def _stalls(root):
    now = datetime.now(CHICAGO)
    mac = {}
    mac_path = os.path.join(root, "mac-status.json")
    if os.path.exists(mac_path):
        with open(mac_path, encoding="utf-8") as handle:
            mac = json.load(handle)
    active = mac.get("active_job") or ""
    progress = mac.get("progress_at") or ""
    for job in snapshot(root)["claimed"]:
        if job["id"] == active and progress:
            try:
                when = datetime.fromisoformat(progress)
                if (datetime.now(when.tzinfo) - when).total_seconds() < 20 * 60:
                    continue
            except ValueError:
                pass
        claimed_at = job.get("claimed_at") or ""
        try:
            when = datetime.fromisoformat(claimed_at)
            age = (datetime.now(when.tzinfo) - when).total_seconds()
        except ValueError:
            continue
        if age < 20 * 60:
            continue
        path = os.path.join(root, "claimed", job["id"] + ".json")
        job["stalled"] = True
        with open(path, "w", encoding="utf-8") as handle:
            json.dump(job, handle)
        fail(root, job["id"])


def dispatch(root):
    env, path = _env()
    os.makedirs(os.path.join(root, "artifacts"), exist_ok=True)
    os.makedirs(os.path.join(root, "state"), exist_ok=True)
    report = {"calendar": None, "qbo": None, "summit_mail": 0, "extract": 0, "synopsis": 0, "hubspot": None}
    try:
        result = calendar_run(root, env)
        if result:
            complete(root, result["id"], result)
            report["calendar"] = result["summary"]
    except Exception as error:
        report["calendar"] = type(error).__name__
    try:
        payload = qbo.pull(root, env, path, recent_sender_names(env))
        if payload:
            enqueue(root, {
                "id": _job_id("qbo-" + datetime.now(CHICAGO).date().isoformat()),
                "trigger_key": "qbo-" + datetime.now(CHICAGO).date().isoformat(),
                "type": "qb_note",
                "vertical": "summit",
                "title": "QuickBooks changes",
                "payload": payload,
            })
            report["qbo"] = f"{payload['invoice_count']} invoices, {len(payload['unbilled'])} unbilled"
    except Exception as error:
        report["qbo"] = type(error).__name__
    try:
        prune_queued_mail(root, env)
        sample = voice_sample(env, "SUMMIT_IMAP_USER", "SUMMIT_IMAP_APP_PASSWORD")
        for item in _summit_messages(env):
            item["voice"] = sample
            job = enqueue(root, {
                "id": _job_id("summit:" + item["message_id"]),
                "trigger_key": "summit:" + item["thread_id"] + ":" + item["message_id"],
                "type": "mail_summit",
                "vertical": "summit",
                "title": item["who"] or item["subject"],
                "received_at": item.get("received_at") or "",
                "payload": item,
            })
            if job:
                report["summit_mail"] += 1
    except Exception as error:
        report["summit_mail"] = type(error).__name__
    try:
        report["extract"] = len(_proposals(root, env))
    except Exception as error:
        report["extract"] = type(error).__name__
    try:
        report["synopsis"] = len(_transcripts(root, env))
    except Exception as error:
        report["synopsis"] = type(error).__name__
    try:
        job = _hubspot(root, env)
        report["hubspot"] = bool(job)
    except Exception as error:
        report["hubspot"] = type(error).__name__
    _stalls(root)
    return report


def finish_mail(env, result):
    account = (result.get("payload") or {}).get("account") or result.get("vertical")
    if account == "summit":
        user_key, password_key = "SUMMIT_IMAP_USER", "SUMMIT_IMAP_APP_PASSWORD"
    else:
        user_key, password_key = "REENGINE_IMAP_USER", "REENGINE_IMAP_APP_PASSWORD"
    if not result.get("draft_body"):
        return result
    append_draft(
        env.get("IMAP_HOST"),
        env[user_key],
        env[password_key],
        result.get("draft_subject") or "Reply",
        result["draft_body"],
    )
    result["summary"] = result.get("summary") or "Draft is in Gmail."
    return result

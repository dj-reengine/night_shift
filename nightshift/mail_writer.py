"""Create a Gmail draft by IMAP APPEND. This module cannot send mail."""

import imaplib
from email.message import EmailMessage

from nightshift.textutil import draft_is_clean


def append_draft(host, user, password, subject, body):
    if not draft_is_clean(subject) or not draft_is_clean(body):
        raise ValueError("Draft text contains AI wording")
    message = EmailMessage()
    message["From"] = user
    message["Subject"] = subject or "Reply"
    message.set_content(body or "")
    client = imaplib.IMAP4_SSL(host or "imap.gmail.com", 993, timeout=30)
    try:
        client.login(user, (password or "").replace(" ", ""))
        client.append("[Gmail]/Drafts", "\\Draft", None, message.as_bytes())
        client.select('"[Gmail]/Drafts"', readonly=False)
        status, data = client.uid("SEARCH", None, "UNDELETED")
        if status == "OK" and data and data[0]:
            newest = data[0].split()[-1]
            try:
                client.uid("STORE", newest, "+X-GM-LABELS", "(AI)")
            except imaplib.IMAP4.error:
                pass
        client.logout()
    except Exception:
        try:
            client.logout()
        except Exception:
            pass
        raise
    return "draft"

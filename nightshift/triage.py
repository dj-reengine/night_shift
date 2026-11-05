"""Section 6 of the ReEngine triage file. Only open REPLY rows become drafts."""


def _cells(line):
    parts = [part.strip() for part in line.strip().strip("|").split("|")]
    return parts


def reply_rows(text):
    """Return open REPLY rows that already have a thread id and a message id."""
    in_open = False
    rows = []
    for line in text.splitlines():
        if line.startswith("## 6."):
            in_open = True
            continue
        if in_open and line.startswith("### "):
            break
        if not in_open or not line.startswith("|"):
            continue
        cells = _cells(line)
        if not cells or cells[0] in ("Flag", "---") or set(cells[0]) <= {"-"}:
            continue
        if cells[0].upper() != "REPLY":
            continue
        while len(cells) < 8:
            cells.append("")
        status = cells[7].lower()
        if "draft-exists" in status or status.startswith("closed"):
            continue
        thread_id = cells[5]
        message_id = cells[6]
        if not thread_id or not message_id:
            continue
        rows.append({
            "who": cells[1],
            "needed": cells[2],
            "thread_id": thread_id,
            "message_id": message_id,
            "status": cells[7],
        })
    return rows

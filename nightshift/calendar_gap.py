"""TDHCA busy/free compared with ReEngine commitments. Read only."""


def is_out_of_office(event):
    if event.get("out_of_office"):
        return True
    title = event.get("title") or ""
    return "out of office" in title.lower()


def is_real_commitment(event):
    if event.get("calendar") == "David Tasks":
        return False
    if is_out_of_office(event):
        return True
    others = [a for a in (event.get("attendees") or []) if not a.get("self")]
    return len(others) > 0


def _overlaps(start_a, end_a, start_b, end_b):
    return start_a < end_b and start_b < end_a


def compare(tdhca_busy, reengine_events):
    """Return TDHCA blocks with nothing on ReEngine, and real ReEngine commitments with no TDHCA block.

    Any ReEngine event opposite a TDHCA block covers it, including a block with no guests.
    Only an out-of-office event or one with another person can be something to add on TDHCA.
    """
    opposite = [event for event in reengine_events if event.get("calendar") != "David Tasks"]
    real = [event for event in opposite if is_real_commitment(event)]
    fill = []
    for block in tdhca_busy:
        covered = any(
            _overlaps(block["start"], block["end"], event["start"], event["end"])
            for event in opposite
        )
        if not covered:
            fill.append({"start": block["start"], "end": block["end"], "kind": "fill"})
    add = []
    for event in real:
        covered = any(
            _overlaps(event["start"], event["end"], block["start"], block["end"])
            for block in tdhca_busy
        )
        if not covered:
            add.append({"start": event["start"], "end": event["end"], "kind": "add", "title": event.get("title") or ""})
    return {"fill": fill, "add": add}

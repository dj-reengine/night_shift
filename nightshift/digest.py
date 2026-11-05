"""Morning headline. First matching line wins. This is not a model call."""

def digest_line(state):
    if state.get("second_failure") or state.get("stalled"):
        return state.get("second_failure") or state.get("stalled")
    if state.get("sensitive_draft"):
        return state["sensitive_draft"]
    if state.get("unbilled"):
        return state["unbilled"]
    if state.get("tdhca_gap_today"):
        return state["tdhca_gap_today"]
    if state.get("drift"):
        return state["drift"]
    return "Queue clear."

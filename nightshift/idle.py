"""When the Mac may start a model job. Numbers are the spec."""

from datetime import datetime
from zoneinfo import ZoneInfo

CHICAGO = ZoneInfo("America/Chicago")
DAY_IDLE_SECONDS = 10 * 60
NIGHT_IDLE_SECONDS = 3 * 60
CPU_START_MAX = 25
CPU_YIELD = 60
YIELD_HOLD_SECONDS = 45
CALL_FINISH_SECONDS = 60


def is_overnight(now):
    local = now.astimezone(CHICAGO)
    minutes = local.hour * 60 + local.minute
    return minutes >= (21 * 60 + 30) or minutes < (6 * 60 + 30)


def gate(on_ac, idle_seconds, cpu_percent, now):
    """Return start, battery, in use, or busy."""
    if not on_ac:
        return "battery"
    needed = NIGHT_IDLE_SECONDS if is_overnight(now) else DAY_IDLE_SECONDS
    if idle_seconds < needed:
        return "in use"
    if cpu_percent >= CPU_START_MAX:
        return "busy"
    return "start"


def should_pause(cpu_high_seconds, call_age_seconds):
    """True when the running job should go back on the queue.

    A model call already underway and under a minute old is allowed to finish.
    """
    if cpu_high_seconds < YIELD_HOLD_SECONDS:
        return False
    if call_age_seconds is not None and call_age_seconds < CALL_FINISH_SECONDS:
        return False
    return True

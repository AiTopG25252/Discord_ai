"""Simple per-user cooldown tracker."""
import time

_last: dict[int, float] = {}

def allowed(user_id: int, cooldown: float = 3.0) -> bool:
    now = time.time()
    if now - _last.get(user_id, 0) < cooldown:
        return False
    _last[user_id] = now
    return True

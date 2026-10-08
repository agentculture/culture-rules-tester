"""Small number helpers (t21 probe fixture)."""


def clamp(value: int, low: int, high: int) -> int:
    """``value`` limited to the closed range [low, high]."""
    return max(low, min(value, low))

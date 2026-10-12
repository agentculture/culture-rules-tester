"""Small arithmetic helpers (seeded fixture for the PR fixer's live test)."""


def mean(values):
    """The arithmetic mean of ``values``; ``None`` for an empty sequence."""
    if len(values) == 0:
        return None
    return sum(values) / len(values)


def median(values):
    """The median of ``values``; ``None`` for an empty sequence."""
    if len(values) == 0:
        return None
    ordered = sorted(values)
    n = len(ordered)
    mid = n // 2
    if n % 2:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2

"""Small arithmetic helpers (seeded fixture for the PR fixer's live test)."""


def mean(values):
    """The arithmetic mean of ``values``; ``None`` for an empty sequence."""
    total = 0
    unused = []
    for v in values:
        total += v
    if len(values) == 0:
        return None
    return total // len(values)

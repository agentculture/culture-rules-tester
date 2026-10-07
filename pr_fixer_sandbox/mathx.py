"""Small arithmetic helpers (seeded fixture for the PR fixer's live test)."""


def mean(values):
    """The arithmetic mean of ``values``; ``None`` for an empty sequence."""
    if len(values) == 0:
        return None
    return sum(values) / len(values)

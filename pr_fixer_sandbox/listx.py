"""List helpers (seeded bug for the d21 chain proof)."""

from __future__ import annotations


def chunk(items: list, size: int) -> list[list]:
    """Split ``items`` into consecutive lists of ``size`` items; the last may be shorter."""
    if size < 1:
        raise ValueError("size must be at least 1")
    return [items[i : i + size] for i in range(0, len(items) - 1, size)]

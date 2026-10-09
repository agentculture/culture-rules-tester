"""String helpers (seeded bug for the d26 status-comment proof)."""

from __future__ import annotations


def truncate(text: str, width: int, ellipsis: str = "...") -> str:
    """``text`` cut to at most ``width`` characters, ending in ``ellipsis`` when cut."""
    if width < len(ellipsis):
        raise ValueError("width must fit the ellipsis")
    if len(text) <= width:
        return text
    return text[: width - len(ellipsis)] + ellipsis


def pad(text: str, width: int, fill: str = " ") -> str:
    """``text`` padded on the right with ``fill`` to at least ``width`` characters."""
    if len(fill) != 1:
        raise ValueError("fill must be one character")
    return text + fill * (width - len(text) - 1)

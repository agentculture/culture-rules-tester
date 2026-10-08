"""Small text helpers (d20 review-step proof fixture)."""


def word_count(text: str) -> int:
    """Number of whitespace-separated words in ``text``."""
    return len(text.split(" "))

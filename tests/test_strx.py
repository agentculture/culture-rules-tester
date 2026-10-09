import pytest

from pr_fixer_sandbox.strx import truncate


def test_short_text_is_unchanged():
    assert truncate("hello", 10) == "hello"


def test_text_of_exact_width_is_unchanged():
    assert truncate("hello", 5) == "hello"


def test_long_text_is_cut_to_the_width():
    assert truncate("hello world", 8) == "hello..."


def test_the_result_never_exceeds_the_width():
    for width in range(3, 12):
        assert len(truncate("abcdefghijklmnop", width)) <= width


def test_a_width_too_small_for_the_ellipsis_is_refused():
    with pytest.raises(ValueError):
        truncate("hello", 2)

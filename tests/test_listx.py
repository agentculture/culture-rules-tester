import pytest

from pr_fixer_sandbox.listx import chunk


def test_chunk_splits_evenly():
    assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]


def test_chunk_keeps_a_short_tail():
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]


def test_chunk_of_one_item():
    assert chunk([7], 3) == [[7]]


def test_chunk_of_nothing():
    assert chunk([], 2) == []


def test_chunk_refuses_a_zero_size():
    with pytest.raises(ValueError):
        chunk([1], 0)

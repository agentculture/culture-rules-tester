from pr_fixer_sandbox.mathx import mean


def test_mean_of_two_values():
    assert mean([1, 2]) == 1.5


def test_mean_of_empty_is_none():
    assert mean([]) is None

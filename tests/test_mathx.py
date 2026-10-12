from pr_fixer_sandbox.mathx import mean


def test_mean_of_two_values():
    assert mean([1, 2]) == 1.5


def test_mean_of_empty_is_none():
    assert mean([]) is None


def test_median_of_unsorted_odd():
    from pr_fixer_sandbox.mathx import median

    assert median([3, 1, 2]) == 2


def test_median_of_unsorted_even():
    from pr_fixer_sandbox.mathx import median

    assert median([4, 1, 3, 2]) == 2.5


def test_median_of_empty_is_none():
    from pr_fixer_sandbox.mathx import median

    assert median([]) is None

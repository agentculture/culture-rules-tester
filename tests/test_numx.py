from pr_fixer_sandbox.numx import clamp


def test_clamp_keeps_a_value_inside_the_range():
    assert clamp(5, 0, 10) == 5


def test_clamp_caps_at_high():
    assert clamp(50, 0, 10) == 10

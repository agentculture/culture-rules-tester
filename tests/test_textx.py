from pr_fixer_sandbox.textx import word_count


def test_word_count_ignores_repeated_spaces():
    assert word_count("a  b") == 2


def test_word_count_of_empty_text_is_zero():
    assert word_count("") == 0

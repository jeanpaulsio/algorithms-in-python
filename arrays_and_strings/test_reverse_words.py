from arrays_and_strings.reverse_words import reverse_words


def test_empty_string():
    assert reverse_words("") == ""


def test_single_letter():
    assert reverse_words("a") == "a"


def test_single_space():
    assert reverse_words(" ") == ""


def test_begins_with_space():
    assert reverse_words(" foo") == "foo"


def test_ends_with_space():
    assert reverse_words("foo ") == "foo"


def test_one_word():
    assert reverse_words("foo") == "foo"


def test_two_words():
    assert reverse_words("foo bar") == "bar foo"


def test_more_than_two_words():
    assert reverse_words("foo bar baz quux") == "quux baz bar foo"

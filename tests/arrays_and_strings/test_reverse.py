from arrays_and_strings.reverse import reverse


def test_empty_array() -> None:
    assert reverse([]) == []


def test_single_element() -> None:
    assert reverse(["a"]) == ["a"]
    assert reverse([1]) == [1]


def test_two_elements() -> None:
    assert reverse(["a", "b"]) == ["b", "a"]
    assert reverse([1, 2]) == [2, 1]


def test_three_elements() -> None:
    assert reverse(["a", "b", "c"]) == ["c", "b", "a"]
    assert reverse([1, 2, 3]) == [3, 2, 1]


def test_multiple_items() -> None:
    assert reverse(["a", 2, "b", 4]) == [4, "b", 2, "a"]

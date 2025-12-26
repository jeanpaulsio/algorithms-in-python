from algorithms.arrays_and_strings.clone_even_numbers import clone_even_numbers


def test_empty_array():
    assert clone_even_numbers([]) == []


def test_single_odd_number():
    assert clone_even_numbers([1]) == [1]


def test_single_even_number():
    assert clone_even_numbers([2, -1]) == [2, 2]


def test_all_odd_numbers():
    assert clone_even_numbers([1, 3, 5]) == [1, 3, 5]


def test_all_even_numbers():
    assert clone_even_numbers([2, 4, 6, -1, -1, -1]) == [2, 2, 4, 4, 6, 6]


def test_mixed_numbers():
    assert clone_even_numbers([1, 2, 3, 4, 5, 6, -1, -1, -1]) == [1, 2, 2, 3, 4, 4, 5, 6, 6]

from arrays_and_strings.two_sum import two_sum


def test_empty_array():
    assert two_sum(nums=[], target=1) is None


def test_single_element():
    assert two_sum(nums=[1], target=1) is None


def test_two_elements_with_sum():
    assert two_sum(nums=[1, 2], target=3) == (0, 1)


def test_two_elements_without_sum():
    assert two_sum(nums=[1, 2], target=4) is None


def test_multiple_elements_with_sum():
    assert two_sum(nums=[1, 2, 7, 11, 15], target=9) == (1, 2)


def test_multiple_elements_without_sum():
    assert two_sum(nums=[1, 2, 7, 11, 15], target=5) is None


def test_duplicate_elements():
    assert two_sum(nums=[1, 2, 4, 4, 15], target=8) == (2, 3)

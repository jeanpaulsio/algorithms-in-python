# See ../../docs/arrays_and_strings/clone_even_numbers.md


def clone_even_numbers(numbers: list[int]) -> list[int]:
    """
    Replaces each even number with two of the same number.

    Given an array of numbers, replace each even number with two of the same number.
    Assume that the array has the exact number of space to accommodate the new numbers.
    Empty slots are represented by -1.

    Level: Easy

    Examples:
        >>> clone_even_numbers([2, 4, 6, -1, -1, -1])
        [2, 2, 4, 4, 6, 6]
    """
    if not numbers:
        return numbers

    i = _find_last_number(numbers)
    j = len(numbers) - 1

    while i >= 0:
        if numbers[i] % 2 == 0:
            numbers[j] = numbers[i]
            j -= 1
        numbers[j] = numbers[i]
        j -= 1
        i -= 1

    return numbers


def _find_last_number(arr: list[int]) -> int:
    """Finds the index of the last non-empty slot (-1)"""
    for i, val in enumerate(arr):
        if val == -1:
            return i - 1

    return len(arr) - 1

def clone_even_numbers(arr):
    """
    Replace each even number with two of the same number.

    Given an array of numbers, replace each even number with two of the same number.
    Assume that the array has the exact number of space to accommodate the new numbers.
    Empty slots are represented by -1.

    Examples:
        >>> clone_even_numbers([2, 4, 6, -1, -1, -1])
        [2, 2, 4, 4, 6, 6]
    """
    if not arr:
        return arr

    i = _find_last_number(arr)
    j = len(arr) - 1

    while i >= 0:
        if arr[i] % 2 == 0:
            arr[j] = arr[i]
            j -= 1
        arr[j] = arr[i]
        j -= 1
        i -= 1

    return arr


def _find_last_number(arr):
    for i, val in enumerate(arr):
        if val == -1:
            return i - 1

    return len(arr) - 1

from typing import Any

# See ../../docs/arrays_and_strings/reverse.md


def reverse(items: list[Any]) -> list[Any]:
    """
    Reverses the order of an array's elements.

    Given an array, reverse the order of its elements in place.

    Level: Easy

    Examples:
        >>> reverse([1, 2, 3, 4])
        [4, 3, 2, 1]
        >>> reverse(["hello", "world"])
        ["world", "hello"]
    """
    i, j = 0, len(items) - 1

    while i < j:
        items[i], items[j] = items[j], items[i]

        i += 1
        j -= 1

    return items

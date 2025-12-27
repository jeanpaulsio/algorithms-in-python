from typing import Any

# See ../../docs/arrays_and_strings/reverse.md


def reverse(items: list[Any]) -> list[Any]:
    """
    Reverse a list in place and return it.

    Problem:
        Given a list, reverse the order of its elements in place
        without using built-in reversal methods.

    Level:
        Easy

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

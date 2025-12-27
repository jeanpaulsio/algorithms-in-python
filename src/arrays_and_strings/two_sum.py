# See ../../docs/arrays_and_strings/two_sum.md


def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    """
    Return indices of two elements whose values sum to the target.

    Problem:
        Given a sorted list of integers and a target integer, return the indices
        of the two numbers such that they add up to the target.
        If multiple valid solutions exist, return any one of them. Return None
        if no such pair exists. Indices are zero-based.

    Level:
        Easy

    Examples:
        >>> two_sum(nums=[2, 7, 11, 15], target=9)
        (0, 1)
    """
    if len(nums) < 2:
        return None

    i, j = 0, len(nums) - 1
    while i < j:
        pair_sum = nums[i] + nums[j]
        if pair_sum == target:
            return i, j
        elif pair_sum < target:
            i += 1
        elif pair_sum > target:
            j -= 1

    return None

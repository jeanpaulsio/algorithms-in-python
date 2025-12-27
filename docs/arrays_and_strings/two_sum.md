# Problem

Given a sorted list of integers and a target integer, return the indices
of the two numbers such that they add up to the target.
If multiple valid solutions exist, return any one of them. Return None
if no such pair exists. Indices are zero-based.


Level: Easy

[See solution](../../src/arrays_and_strings/two_sum.py)

## Approach

Use two pointers on the sorted list, pointer `i` starting at the beginning and
pointer `j` starting at the end. At each step, compare the sum of the pointed
values to the target. If the sum is too small, move pointer `i` forward (to the right).
If the sum is too large, move pointer `j` backwards (to the left). Continue until
a matching pair is found or the pointers cross.

## Insights

- The sorted order gives us monotonic control over the sum.
- Moving the left pointer strictly increases the sum.
- Moving the right pointer strictly decreases the sum.
- Each pointer move eliminates a set of impossible pairs, so we never need to revisit
elements


## Edge Cases

- Empty array
- Single element

## Time Complexity

- O(n) where n is the length of the the array.
- In the worst case, we scan across the list once so the total number of
operations grows linearly with the size of the input.

## Space Complexity

- O(1) because we use a constant amount of space. No additional data structures required.


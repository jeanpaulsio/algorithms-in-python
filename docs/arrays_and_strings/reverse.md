# Problem

Given an array, reverse the order of its elements in place.

Level: Easy

[See solution](../../src/arrays_and_strings/reverse.py)

## Approach

Use two pointers starting at opposite ends of the array. Swap elements at these
positions and move the pointer towards the center until they meet.

## Insights

- The invariant condition is that elements outside of the current `[i, j]` range
are in their final positions.
- When `i` is greater or equal to `j`, that means that all elements have been swapped.


## Time Complexity

- O(n) where n is the length of the array
- Each element is visited once during the reversal process

## Space Complexity

- O(1) because we modify the array in place without allocating any addditional data
structure.

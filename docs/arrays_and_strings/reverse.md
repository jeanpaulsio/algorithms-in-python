# Problem

Given an array, reverse the order of its elements in place.

## Approach

Use two pointers starting at opposite ends of the array. Swap elements at these positions and move the pointer towards the center until they meet.

## Insights

After each swap, elements outside of the `[i, j]` range are in their final positions. When `i` is greater than or equal to `j`, that means that all elements have been swapped.

## Time Complexity

- `O(n)`
- each element is visited once

## Space Complexity

- `O(1)`
- the array is modified in place and only pointer variables are used

# Problem

Given an array of numbers, replace each even number with two of the same number.
Assume that the array has the exact number of space to accommodate the new numbers.
Empty slots are represented by -1.

Level: Easy

[See solution](../../src/arrays_and_strings/clone_even_numbers.py)

## Approach

Use two pointers, both starting from the right side of the array. Pointer `i` starts
at the last actual number (before the first -1 marker). Pointer `j` starts at the
end of the array. Process elements backwards. For each element at `i`, if it's even,
copy it twice to positions `j` and `j-1`. If it's odd, only copy it once to position
`j`. Decrement `j` by the number of copies made and decrement `i` to move to the next
element.

## Insights

- Working backwards by processing from right to left ensures that we never overwrite
unprocessed elements. If we processed from left to right, we'd lose data that we
haven't processed.
- The invariant condition is that everything ot the right of pointer `j` is correctly
placed.
- Pointer `i` tracks the current element being processed while pointer `j` tracks
where to write the next element(s).

## Time Complexity

- O(n) where n is the length of the array.
- We iterate through the array once with both pointers and each element is processed
only once.

## Space Complexity

- O(1) because we modify the array in place without allocating any addditional data
structure.

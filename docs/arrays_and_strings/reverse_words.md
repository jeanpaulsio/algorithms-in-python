# Problem

Given a string, return a new string with the words in reverse order.
Words are separated by spaces. Leading and trailing spaces are ignored.

Level: Easy

[See solution](../../src/arrays_and_strings/reverse_words.py)

## Approach

Use two pointers, both starting from the right side of the string. Pointer `i`
starts at the last character index and pointer `j` starts at the end of the string.
Move pointer `i` backwards from right to left. When `i` encounters a space, extract
the word between `i + 1` and `j`, append it to the string result, then move `j`
to `i`'s position. Continue until `i` reaches the beginning. After the loop, handle
the first word separately since it won't have a leading space.


## Insights

- Working backwards allows us to extract words in reverse order naturally.
- Pointer `j` marks the end of the current word being processed while pointer `i`
searches backwards for word boundaries.
- The invariant condition is that all words to the right of pointer `j` have already
been added to the result in reverse order.
- We need to handle the first word separately after the loop because it doesn't have
a leading space to trigger extraction.


## Edge Cases

- Empty string
- Single letter
- Single space
- Begins with space
- Ends with space

## Time Complexity

- O(n) where n is the length of the string.
- We iterate through the string once with `i` and each character is examined once.

## Space Complexity

- O(n) where n is the length of the string
- We build a new result string that contains all the words from the input string.
- The space required is proportional to the input size.


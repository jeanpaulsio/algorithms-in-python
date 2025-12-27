def reverse_words(s):
    """
    Reverse the order of words in a string.

    Given a string, return a new string with the words in reverse order.
    Words are separated by spaces. Leading and trailing spaces are ignored.

    Level: Easy

    Examples:
        >>> reverse_words("foo bar")
        'bar foo'
        >>> reverse_words("foo bar baz quux")
        'quux baz bar foo'
        >>> reverse_words(" foo")
        'foo'
        >>> reverse_words("foo ")
        'foo'
    """
    result = ""
    i = len(s) - 1
    j = len(s)

    while i >= 0:
        if s[i] == " ":
            word = s[i + 1 : j]
            if word:
                result += word
            if result and i > 0:
                result += " "
            j = i
        i -= 1

    last_word = s[i + 1 : j]
    if last_word != " ":
        result += last_word

    return result

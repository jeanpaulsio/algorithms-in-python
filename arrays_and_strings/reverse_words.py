def reverse_words(s):
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

def clone_even_numbers(arr):
    if not arr:
        return arr

    i = _find_last_number(arr)
    j = len(arr) - 1

    while i >= 0:
        if arr[i] % 2 == 0:
            arr[j] = arr[i]
            j -= 1
        arr[j] = arr[i]
        j -= 1
        i -= 1

    return arr

def _find_last_number(arr):
    for i, val in enumerate(arr):
        if val == -1:
            return i - 1

    return len(arr) - 1

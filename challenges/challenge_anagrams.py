def is_anagram(first_string, second_string):
    first_string = first_string.lower()
    second_string = second_string.lower()

    sorted_first = sort_string(first_string)
    sorted_second = sort_string(second_string)

    return sorted_first, sorted_second, sorted_first == sorted_second


def sort_string(string):
    if len(string) <= 1:
        return string

    mid = len(string) // 2
    left = sort_string(string[:mid])
    right = sort_string(string[mid:])

    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return "".join(merged)

def freq_digit(num: int) -> int:
    int_as_str = str(num)
    max_count, related_number = -1, -1
    for x in range(1, 11):
        count = int_as_str.count(str(x))
        if count > max_count:
            max_count = count
            related_number = x
    return related_number

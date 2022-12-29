def is_armstrong(n: int) -> bool:
    # An armstrong number is a number that is the sum of its own digits
    # each raised to the power of the number of digits

    power = len(str(n))
    total = 0
    for digit in str(n):
        total += int(digit) ** power

    return total == n

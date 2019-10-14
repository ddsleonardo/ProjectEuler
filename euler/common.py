import math

def digit_count(n: int):
    count = 1
    while (n >= 10):
        n = n // 10
        count = count + 1

    return count
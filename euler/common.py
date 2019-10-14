import math

def digit_count(n: int):
    count = 1
    while (n >= math.pow(10, count)):
        count = count + 1

    return count
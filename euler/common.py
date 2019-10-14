import math

def is_prime(n: int):
    ''' For a given integer n, returns true if
        n is a prime number '''

    if (n < 4):
        return n > 1

    if (n % 2 == 0 or n % 3 == 0):
        return False

    div = 5

    while (div * div <= n):
        if (n % div == 0 or n % (div + 2) == 0):
            return False
        div += 6

    return True
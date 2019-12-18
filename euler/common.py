import math

def is_prime(n: int, p_list: list = []):
    ''' For a given integer n, returns true if
        n is a prime number '''

    if (n < 4):
        return n > 1

    if (n % 2 == 0 or n % 3 == 0):
        return False

    if (len(p_list) == 0):
        div = 5

        while (div * div <= n):
            if (n % div == 0 or n % (div + 2) == 0):
                return False
            div += 6
    else:
        i = 0
        while (p_list[i] * p_list[i] <= n):
            if (n % p_list[i] == 0):
                return False;

            i += 1

    return True

def next_prime(n: int, p_list: list = []):
    ''' Returns the smallest prime
    that is greater than n'''
    if (n < 2):
        return 2

    if (n == 2):
        return 3

    if (n % 6 == 5 and is_prime(n + 2, p_list)):
        return n + 2

    n += 1
    n += (5 - n % 6)
    while True:
        if (is_prime(n, p_list)):
            return n
        if (is_prime(n + 2, p_list)):
            return n + 2

        n += 6

def is_permutation(a: int, b: int):
    ''' Returns true if the one of the two given integers
    can be obtained by a permutation of the digits of the other'''

    if (len(str(a)) != len(str(b))):
        return False

    # Try the sum first
    if (sum_digits(a) != sum_digits(b)):
        return False

    str_a = str(a)
    str_b = str(b)

    digits_a = [str_a[i] for i in range(len(str_a))]
    digits_b = [str_b[i] for i in range(len(str_b))]

    # For each digit in a, we try to remove it from b
    # If they are permutations of each other, this will never return an error
    for digit in digits_a:
        try:
            i = digits_b.remove(digit)
        except ValueError:
            return False

    return True

def sum_digits(n: int):
    ''' Returns the sum of the digits of a given integer n'''

    sum = 0
    while n:
        sum += n % 10
        n //= 10

    return sum

def large_power_mod(base: int, exponent: int, mod: int):

    if (base == 0):
        return 0
    if (exponent == 0):
        return 1

    # First of all try to reduce the base
    base %= mod
    res = 1

    # Logic: base^exponent = product of base^(powers of 2),
    # looping over all powers of 2 you'd need to add in order to get exponent
    while (exponent > 0):
        exp_2 = 1
        base_power_power_n = base
        while (2 ** exp_2 <= exponent):
            base_power_power_n *= base_power_power_n
            base_power_power_n %= mod
            exp_2 += 1

        res *= base_power_power_n
        res %= mod
        exponent -= (2 ** (exp_2 - 1))

    return res
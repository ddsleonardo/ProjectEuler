### https://www.projecteuler.net/problem=684

import sys
sys.path.append(r'..\euler')
import common as euler
import time

def return_smallest_digit_sum(n: int, mod: int):
    ''' Returns the smallest integer (mod n)
    whose digit sum equals n '''

    # If n = 9 * k, this number is 9 repeated k times = (10 ^ k - 1)
    # Therefore if n = 9 * k + r, this number is (1 + r) * (10 ^ k - 1) + r
    # If r = 0 we get the first formula!
    k = n // 9

    return ((n % 9 + 1) * (euler.large_power_mod(10, k, mod) - 1) + (n % 9)) % mod

def return_sum_until_n(n: int, mod: int):

    # If n % 9 == 0, this has a very simple formula:
    # returm_sum_until_n(9 * k) = 6 * (10 ^ k - 1) - 9 * k
    # Therefore for any number, we write it as n = 9 * k + r, use the formula for 9 * k,
    # then calculate the rest one by one
    k = n // 9
    
    return ((6 * (euler.large_power_mod(10, k, mod) - 1) - 9 * k) % mod) + (sum([return_smallest_digit_sum(i, mod) for i in range(n - n % 9 + 1, n + 1)]) % mod)

def Problem684(n: int):
    ''' Returns the sum defined in the problem 
    for the n-th Fibonacci number'''

    # Initialise some constants
    start_time = time.time()
    res = 0

    f0 = 0
    f1 = 1
    count = 2
    while (count <= n):
        f_count = f0 + f1
        print ('%d %d' % (count, f_count))
        res += return_sum_until_n(f_count, (10**9 + 7))
        res %= (10**9 + 7)
        f0, f1 = f1, f_count
        count = count + 1

    # Return result and time elapsed
    return res, '%.3f s' % (time.time() - start_time)
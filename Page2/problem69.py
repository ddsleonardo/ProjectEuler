### https://www.projecteuler.net/problem=69

import sys
sys.path.append(r'..\euler')
import euler.common as euler
import time

# From the formula for the totient function, we get that:
# n/phi(n) = 1 / prod (1 - 1/p) for p prime dividing n
# n/phi(n) = prod (p) / prod (p - 1), for p prime dividing n
# Therefore it seems that you maximise this fraction by taking
# all primes from 2 onwards

def Problem69(n: int):

    # Initialise some constants
    start_time = time.time()
    primes = [2]
    res = 1

    while (res * primes[-1] < n):
        res *= primes[-1]
        primes.append(euler.next_prime(primes[-1]))

    print ('%d - %.3f' % (res, 10**6 * (time.time() - start_time)))
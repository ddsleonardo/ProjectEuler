### https://www.projecteuler.net/problem=500

import sys
sys.path.append(r'..\euler')
import common as euler
import time

def Problem500(n: int):
    ''' Finds the smallest number with 2^n divisors'''

    # Initialise some numbers
    start_time = time.time()
    primes = [2]
    count = 1

    # The obvious candidate is the multiplication
    # of the first n primes once
    while (count < n):
        primes.append(euler.next_prime(primes[-1]))
        count += 1

    first_prime = 0
    last_prime = count - 1
    exp_to_add = 2

    # Now we replace the largest prime factors by repeated lowest prime factors
    # without changing the number of divisors
    while (primes[first_prime]**exp_to_add < primes[last_prime]):
        primes[last_prime] = primes[first_prime]**exp_to_add
        last_prime -= 1
        exp_to_add *= 2
        if (primes[first_prime]**exp_to_add > primes[last_prime]):
            first_prime += 1
            exp_to_add = 2

    # Now we calculate the number mod 500500507
    res = 1
    index = 0
    while (index < n):
        res *= primes[index]
        res %= 500500507
        index += 1

    print ('%d, %.3fs' % (res, time.time() - start_time))
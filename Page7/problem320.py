### https://www.projecteuler.net/problem=320

import sys
sys.path.append(r'..\euler')
import euler.common as euler
import time
import math

# https://math.stackexchange.com/questions/642216/factorials-and-prime-factors
def prime_exponent_in_factorial(n: int, p: int):

    res = 0
    q = p
    while (n >= q):
        res += n // q
        q *= p

    return res

# Given the prime factorisation of (i!), the p.f. of
# I = (i!)**1234567890 is the p.f. of i! with all exponents
# multiplied by 1234567890

# To find the lowest n such that n! is divisible by I,
# the p.f. of n has to contain all prime factors of I
# with an exponent equal or higher than that of I

# Let p be a prime less than n, then n! has the prime factor p
# a number k of times, where:
# k = sum of int(n / p**j), for j from 1 until int(n / p**j) == 0

# We will approximate this by sum (n / p**j), j > 0,
# because we need to solve for n, and then go from there

def largest_n_divisible(i: int):

    start_time = time.time()
    prime_factors = []
    for p in range(len(primes)):
        if primes[p] > i:
            break
        else:
            prime_factors.append( { 'p' : primes[p], 'e' : prime_exponent_in_factorial(i, primes[p]) } )

    #print ('Time spent factoring: %.3fms' % (1000 * (time.time() - start_time)))
    #start_time = time.time()
    E = 1234567890

    for prime in prime_factors:
        n = prime['e'] * E
        j = int(math.log(n, prime['p']))
        #N = (n * (prime['p'] ** j) * (prime['p'] - 1)) // (prime['p'] ** j - 1)
        # We can approximate N by the simplified formula below
        N = n * (prime['p'] - 1)
        N -= (N % prime['p'])

        # N is just an approximation for now, so we need to find the exact correct value
        # First we go up if we're below the answer
        while (prime_exponent_in_factorial(N, prime['p']) < n):
            N += prime['p']

        # Then we go down if we're above or equal - this is to ensure we'll find the lowest N
        while (prime_exponent_in_factorial(N, prime['p']) >= n):
            N -= prime['p']

        # Add prime['p'] to answer because on the loop above we went down one too many times
        prime['n'] = N + prime['p']

    #print ('Time finding answer: %.3fms' % (1000 * (time.time() - start_time)))
    prime_factors.sort(key=lambda x: x['n'], reverse=True)
    print (i)
    for t in range(3):
        print (prime_factors[t], ((prime_factors[t]['p'] - 1) * prime_factors[t]['e']))

    return max([prime['n'] for prime in prime_factors])
    
def Problem320(u: int):

    # Let's define some constants first
    start_time = time.time()
    res = 0
    primes = [2]
    factors = [{}, {}, { 2 : 1 }]

    # First of all, let's build the prime factorisation
    # for all numbers from 3 to u - we need this for later
    for p in range(3, u + 1):
        if (euler.is_prime(p, primes)):
            primes.append(p)
            factors.append({p : 1})
        else:
            i = 0
            while (p % (primes[i]) != 0):
                i += 1
            factors.append( { k : factors[p // primes[i]][k] for k in factors[p // primes[i]]} )
            try:
                factors[-1][primes[i]] += 1
            except:
                factors[-1][primes[i]] = 1

    # Now we do some initialisation, starting at number 10
    # factor_count is a dictionary that will record the number
    # of occurrences of each prime factor in the number i!
    factor_count = {}

    for p in primes:
        if p > 10:
            break
        else:
            factor_count[p] = 0

    for p in range(2, 10):
        for f in factors[p]:
            factor_count[f] += factors[p][f]

    sorting_time = 0
    calculating_time = 0

    e = 1234567890
    previous_f = 0

    # Now we loop from 10 to u
    for i in range(10, u + 1):

        # First of all, we increment the factor count
        # with the prime factors of i
        for f in factors[i]:
            try:
                factor_count[f] += factors[i][f]
            except:
                factor_count[f] = factors[i][f]

        # We only need to check the prime factors that have been added to,
        # plus the prime factor that was previously limiting, if any
        # This is because the limiting prime factor can only be either the previous
        # or one of the prime factors whose exponent has just now been increased
        if (previous_f == 0):
            primes_tocheck = [p for p in factor_count]
        else:
            primes_tocheck = [p for p in factors[i]] + [previous_f]

        N = 0
        j = 0
        for p in primes_tocheck:
            E = e * factor_count[p] 
            n = E * (p - 1)
            n -= (n % p)

            # N is just an approximation for now, so we need to find the exact correct value
            # First we go up if we're below the answer
            while (prime_exponent_in_factorial(n, p) < E):
                n += p

            # Then we go down if we're above or equal - this is to ensure we'll find the lowest N
            while (prime_exponent_in_factorial(n, p) >= E):
                n -= p

            # Add prime['p'] to answer because on the loop above we went down one too many times
            if (n + p > N):
                N = n + p
                previous_f = p
                    
        res += N

    print ('%d - Time: %6fs' % (res, time.time() - start_time))
    return res
### https://www.projecteuler.net/problem=49

import sys
sys.path.append(r'..\euler')
import common as euler
import time

def Problem49():
    ''' Supposedly solves Problem 49!'''

    # Initialise some numbers
    start_time = time.time()
    res = 0
    n = euler.next_prime(1000)
    primes = {}
    permutations = []

    while (n < 10000):
        s = euler.sum_digits(n)
        if s in primes:
            primes[s].append(n)
        else:
            primes[s] = [n]

        n = euler.next_prime(n)
        
    for k in primes:
        while (len(primes[k]) > 0):
            candidate_permutation = [p for p in primes[k] if euler.is_permutation(primes[k][0], p)]
            if (len(candidate_permutation) > 2):
                permutations.append(candidate_permutation)

            primes[k] = [p for p in primes[k] if p not in candidate_permutation]

    for permutation in permutations:
        for i in range(len(permutation) - 2):
            for j in range(i + 1, len(permutation) - 1):
                if (2 * permutation[j] - permutation[i]) in permutation:
                    print ('%d%d%d' % (permutation[i], permutation[j], (2 * permutation[j] - permutation[i])))

    return res, '%.3f s' % (time.time() - start_time)
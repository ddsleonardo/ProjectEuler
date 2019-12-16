### https://www.projecteuler.net/problem=267

import sys
sys.path.append(r'..\euler')
import common as euler
import time
import math

def combination(n: int, k: int):
    
    res = 1

    if (n == k or k <= 0):
        return res
        
    k, k_ = min(k, n - k), max(k, n - k)
    num = [i for i in range(k_ + 1, n + 1)]
    den = [i for i in range(2, k + 1)]

    while (len(den) > 0):
        q = den[0]
        count = 0
        for i in range(len(den)):
            while (den[i] % q == 0):
                den[i] //= q
                count += 1

        j = 0
        while (count > 0):
            while (num[j] % q == 0 and count > 0):
                num[j] //= q
                count -= 1
            j += 1

        den = [i for i in den if i > 1]

    for i in num:
        res *= i
    #    res %= mod

    return res

def Problem267():
    '''
    Let n be the number of tosses, and h the number of heads.
    Your final capital is: ((1 + 2f)**h) * ((1 - f)**(n - h))

    To maximise probability, you need to find f such that
    the h that solves ((1 + 2f)**h) * ((1 - f)**(n - h)) = 10**9
    is minimal.

    Then the probability that you win is (C(n, h) + C(n, h + 1) + ... + C(n, n)) / 2 ** n
    '''

    # Initialise some constants
    start_time = time.time()
    h = 334
    n = 1000

    # Let's find the minimal h
    while (h < n):
        f = (3 * h) / (2 * n) - 0.5
        if ((1 + 2 * f)**h) * ((1 - f)**(n - h)) > 10**9:
            break
        else:
            h += 1

    # Now let's find the probability given h
    p = sum([combination(n, i) for i in range(h, n + 1)])
    p /= (2**1000)

    print (('%.12f, time = %.3fms') % (p, 1000 * (time.time() - start_time)))
### https://www.projecteuler.net/problem=57

import sys
sys.path.append(r'..\euler')
import common as euler
import time

def Problem57(n: int):
    ''' For a positive integer n, returns the count
        of iterations, from 1 to n, where the numerator
        exceeds the denominator in number of digits'''
    start_time = time.time()

    # Initialise count and initial fraction    
    count = 0
    num, den = 1, 2

    for i in range(1, n + 1):
        # Check if 1 + num/den = (num + den)/den satisfies the condition
        if (euler.digit_count(num + den) > euler.digit_count(den)):
            count = count + 1

        # Calculate the next iteration, num*/den* = 1 / (2 + num / den)
        num, den = den, (num + 2 * den)

    return count, '%.3f s' % (time.time() - start_time)
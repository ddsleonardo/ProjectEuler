### https://www.projecteuler.net/problem=57

import sys
sys.path.append(r'..\euler')
import common as euler
import time

def Problem57(n: int):
    ''' For a positive integer n, returns the count
        of iterations, from 1 to n, where the numerator
        exceeds the denominator in number of digits'''

    # Initialise count and initial fraction
    start_time = time.time()
    count = 0
    num, den = 1, 2

    for i in range(1, n + 1):
        # Check if 1 + num/den = (num + den)/den satisfies the condition
        if (len(str(num + den)) > len(str(den))):
            count = count + 1

        # Calculate the next iteration, num*/den* = 1 / (2 + num / den)
        num, den = den, (num + 2 * den)

    # Return result and time elapsed
    return count, '%.3f s' % (time.time() - start_time)
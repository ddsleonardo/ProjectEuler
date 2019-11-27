### https://www.projecteuler.net/problem=85

import sys
sys.path.append(r'..\euler')
import common as euler
import time
import math

def Problem85(k: int):
    '''
    Returns the area of the rectangle whose
    sub-rectangle count is closest to k
    '''
    
    # Initialise time and some values
    start_time = time.time()
    min_delta = 10**9
    min_area = 0

    def count_rectangles(m, n):
        return m * n * (m + 1) * (n + 1) / 4

    max_m = int(math.sqrt((math.sqrt(1 + 16 * k) - 1) / 2)) + 1

    for m in range(1, max_m + 1):
        n_exact = (math.sqrt(m**2 * (m + 1)**2 + 16 * k * m * (m + 1)) - m * (m + 1))/ (2 * m * (m + 1))
        for p in range(int(n_exact), int(n_exact) + 2):
            if math.fabs(count_rectangles(m, p) - k) < min_delta:
                min_delta = math.fabs(count_rectangles(m, p) - k)
                min_area = m * p
                print ('Closest count to k: %d (m = %d, n = %d)' % (count_rectangles(m, p), m, p))

    return min_area, '%.6f s' % (time.time() - start_time)
### https://www.projecteuler.net/problem=79

import sys
sys.path.append(r'..\euler')
import common as euler
import time
import math

def partition_count(i: int, n: int, part: list):
    ''' Calculates the number of partitions (modulo n) of the given
    integer i- requires a list of all partitions up to (i - 1)'''

    # Using https://en.wikipedia.org/wiki/Partition_function_(number_theory)#Recurrence_relations
    count = 0
    k_lower = -1 * int((math.sqrt(24 * i + 1) - 1) / 6)
    k_upper = int((math.sqrt(24 * i + 1) + 1) / 6)
    for k in [k_value for k_value in range(k_lower, k_upper + 1) if k_value != 0]:
        count += math.pow(-1, k + 1) * part[int(i - k * (3 * k - 1) / 2)]

    return int(count % n)

def Problem79(n: int):
    ''' Returns the smallest number whose partition
    count is divisible by n'''

    # Initialise count and initial fraction
    start_time = time.time()
    part = [1, 1]
    while True:
        part.append(partition_count(len(part), n, part))
        
        # If this partition count is 0 modulo n, return result and time elapsed
        if (part[-1] % n == 0):
            return len(part) - 1, '%.3f s' % (time.time() - start_time)
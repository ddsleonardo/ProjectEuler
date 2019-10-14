### https://www.projecteuler.net/problem=58

import sys
sys.path.append(r'..\euler')
import common as euler
import time

def Problem58(n: float):
    ''' For a number 0 < n < 1, returns the side length
        of the square for which the proportion of primes
        along the diagonals is less than n'''

    # Initialise the spiral with side length 3
    start_time = time.time()
    diagonal = [1, 3, 5, 7, 9]
    side_length = 3
    prime_count = 3
    
    # Note that the ratio is not monotonically decreasing
    # However since the question asks for the first time it drops below n, this will do
    while (prime_count / len(diagonal) >= n):
        # Update the side length and step between each new number
        side_length += 2
        step = side_length - 1

        # At each new layer, we need to generate 4 new numbers
        # Add them to the diagonal, and to the prime counter if necessary
        for i in range(4):
            new_number = diagonal[-1] + step
            if (euler.is_prime(new_number)):
                prime_count += 1
            diagonal.append(new_number)
            
    return side_length, '%.3f s' % (time.time() - start_time)
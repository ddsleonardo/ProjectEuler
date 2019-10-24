### https://www.projecteuler.net/problem=43

import sys
sys.path.append(r'..\euler')
import common as euler
import time

def has_duplicate_digits(n: int):
    ''' Returns true if the integer n has
    at least one repeated digit'''
    digits = [dig for dig in str(n)]
    digits.sort()

    for i in range(len(digits) - 1):
        if (digits[i] == digits[i + 1]):
            return True

    return False

def add_next_digit(n: list, div: list):
    ''' Given a number n and a list of divisors,
    adds the next digit so that the three left-most
    digits will divide the given divisor, as
    stated by the problem.'''
    cumulative_sum = 0
    digits = [str(i) for i in range(10) if str(i) not in n]
    for i in digits:
        # Check if adding i as a digit satisfy the divisibility condition
        if ((100 * int(i) + 10 * int(n[0]) + int(n[1])) % div[0] == 0):
            # If we have more than one remaining divisor to satisfy, call the function recursively
            if (len(div) > 1):
                cumulative_sum += add_next_digit([i] + n, div[1:])
            # If we are left with only one divisor to deal with (which will be 2), and two digits to fit, then they can be fit both ways
            else:
                new_number = [int(dig) * (10 ** ((len(n) + 1) - ndx)) for ndx, dig in enumerate([dig for dig in digits if dig is not i] + [i] + n)]
                print ('Found new number: %i' % sum(new_number))
                cumulative_sum += sum(new_number)

    return cumulative_sum

def Problem43():
    ''' Returns the sum of all pandigital numbers
    satistying the problem conditions'''

    # Initialise time
    start_time = time.time()
    res = 0

    i17 = 1
    while (i17 * 17 < 1000):
        # Starting by defining the number as a multiple of 17
        num = i17 * 17
        if (not has_duplicate_digits(num)):
            digits = [dig for dig in str(num)]
            if (num < 100):
                digits.insert(0, '0')
                
            # For each multiple of 17 with no repeated digits, loop through each divisor adding digits
            res = res + add_next_digit(digits, [13, 11, 7, 5, 3, 2])
                
        i17 = i17 + 1

    # Return result and time elapsed
    return res, '%.3f s' % (time.time() - start_time)
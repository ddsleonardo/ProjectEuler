### https://www.projecteuler.net/problem=684

import sys
sys.path.append(r'..\euler')
import common as euler
import time

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

def constrained_combination(n: int, k: int, m: int, mod: int):
    res = 0
    i = 0
    while (i <= k and i <= n/(m + 1)):
        res += (-1)**i * combination(k, i) * combination(n + k - 1 - i * (m + 1), k - 1)
        i += 1

    #while (res < 0):
    #    res += mod

    return res

def mth_digit_sum_n(n: int, m: int, mod: int):
    
    min_digits = 1 + (n - 1) // 9
    leading_digits = []

    count = 0
    extra_digits = 0
    candidate_next_digit = n % 9

    # Logic here is:
    # Loop through candidate digits from 1 to 9 (or from known min first digit if digit count is minimal)
    # If by setting that digit, we do not generate enough possible combinations ahead to reach count == m, we try the next
    # When we first find a digit that can give more combinations than we need, we set that digit and check the next
    # Eventually we will reach count == m, when we do we need to complete the remaining digits with the highest possible each time
    
    # This solves the base cases, but not quick enough for very large n
    # Further work: find out what the next digit that I have to play with - i.e. for n = 10**12, I know the first digit is 3
    # Then I keep looping uselessly finding a bunch of 9, because 8 is not enough to generate the combinations

    while (count < m):
        digits_to_determine = min_digits + extra_digits - len(leading_digits) - 1
        count_gaps_to_9 = 9 * digits_to_determine - ((n - sum(leading_digits)) - candidate_next_digit)
        new_combinations = constrained_combination(count_gaps_to_9, digits_to_determine, 9, 10**9 + 7)
        print ('Calculated constrained combination for %d gaps in %d digits' % (count_gaps_to_9, digits_to_determine))
        if (count + new_combinations > m):
            leading_digits.append(candidate_next_digit)
            candidate_next_digit = max(0, n - sum(leading_digits) - 9 * (digits_to_determine - 1))

        elif (count + new_combinations < m):
            candidate_next_digit += 1
            if (candidate_next_digit == 10 or candidate_next_digit > n):
                candidate_next_digit = 1
                extra_digits += 1

            count += new_combinations

        elif (count + new_combinations == m):
            leading_digits.append(candidate_next_digit)
            for i in range(digits_to_determine):
                leading_digits.append(min(9, n - sum(leading_digits)))

            count += new_combinations

    res = 0
    for i, k in enumerate(leading_digits):
        res += k * euler.large_power_mod(10, len(leading_digits) - i - 1, mod)
        res %= mod

    return res

def Problem685(n: int):
    ''' For a given number of players n,
    return the expected payout for the game winner'''

    # Initialise some constants
    start_time = time.time()
    res = 0

    # use this: https://math.stackexchange.com/questions/98065/how-many-ways-can-b-balls-be-distributed-in-c-containers-with-no-more-than/98144#98144
    for i in range(1, n + 1):
        res += mth_digit_sum_n(i**3, i**4, 10**9 + 7)
        print (i)
        res %= (10**9 + 7)

    # Return result and time elapsed
    return res, '%.3f s' % (time.time() - start_time)

if __name__ == '__main__':
    Problem685(0)
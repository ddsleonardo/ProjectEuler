### https://www.projecteuler.net/problem=62

import sys
sys.path.append(r'..\euler')
import common as euler
import time

def Problem62(n: int):
    ''' For a positive integer n, returns the smallest
    cube that has n digit permutations which are also cubes'''

    # Initialise some numbers
    start_time = time.time()
    digits = 1
    cubes = {}
    permutations = []

    if (n == 1):
        return 1

    i = 1
    while True:
        new_cube = i * i * i

        # If we hit a number with more digits than the previous, we can reset the problem
        if (len(str(new_cube)) > digits):
            cubes = {}
            permutations = []
            digits += len(str(new_cube))

        found_permutation = False
        # First of all, let's try to find a permutation in the existing permutation groups
        for permutation in permutations:
            if (euler.is_permutation(new_cube, permutation[0])):
                found_permutation = True
                permutation.append(new_cube)
                # If this permutation has now reached n items, we return the smallest (always the first) number
                if (len(permutation) == n):
                    return permutation[0], '%.3f s' % (time.time() - start_time)

        # If we didn't find any permutations so far, we search for one amongst the so far unused cubes
        if (not found_permutation):
            # cubes is a dict where values are grouped by a key which is the digit sum
            # this is useful because all candidate permutations will necessary have equal digit sum
            key = euler.sum_digits(new_cube)
            if (key in cubes):
                for cube in cubes[key]:
                    # If we find a permutation, we insert the new pair in the permutations list
                    # We also remove the cube from the singles collection, for we don't need to check it again
                    if (euler.is_permutation(new_cube, cube)):
                        found_permutation = True
                        permutations.append([cube, new_cube])
                        cubes[key].remove(cube)
                        # In the special case where n is 2, the first found permutation gives us the result
                        if (n == 2):
                            return cube, '%.3f s' % (time.time() - start_time)

                #If no permutations were found, we add this to the singles list
                if (not found_permutation):
                    cubes[key].append(new_cube)

            else:
                cubes[key] = []
                cubes[key].append(new_cube)

        i = i + 1
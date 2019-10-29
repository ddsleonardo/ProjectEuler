### https://www.projecteuler.net/problem=683

import sys
sys.path.append(r'..\euler')
import common as euler
import time
import numpy

def get_recursion_coefficients(p: int, n: int):
    ''' For a given starting position p in a table of n players,
    returns the coefficients of the recursive relation between the
    expected number of moves from the position p and those
    of its neighbours'''

    coeff = {}
    prob = [0.1111111111111111, 0.2222222222222222, 0.3333333333333333, 0.2222222222222222, 0.1111111111111111]
    for i, v in enumerate(range(p - 2, p + 3)):
        if (v < 0):
            v = n + v
        elif (v >= n):
            v = v - n
        if (v not in coeff):
            coeff[v] = prob[i]
        else:
            coeff[v] += prob[i]

    coeff.pop(0, None)
    coeff[p] -= 1

    return coeff

def Problem683(n: int):
    ''' For a given number of players n,
    return the expected payout for the game winner'''

    # Initialise some constants
    start_time = time.time()

    matrix_A = [[] for i in range(n - 1)]
    matrix_X = [0 for i in range(n - 1)]

    for index, dist in enumerate(range(1, n)):
        matrix_A[index] = [0 for col in range(n - 1)]

        coeff = get_recursion_coefficients(dist, n)
        for col in coeff:
            matrix_A[index][col - 1] += coeff[col]

        matrix_X[index] = 1

    # I used this: https://en.wikipedia.org/wiki/Discrete_phase-type_distribution
    # Coming from here: https://en.wikipedia.org/wiki/Stochastic_matrix
    matrix_A = numpy.array(matrix_A)
    inv_A = numpy.linalg.inv(matrix_A)
    higher_moment_A = numpy.matmul(inv_A, inv_A)
    higher_moment_A = 2 * numpy.matmul(higher_moment_A, numpy.add(matrix_A, numpy.identity(n - 1)))

    e_k = numpy.linalg.solve(numpy.array(matrix_A), numpy.array(matrix_X))
    e_k2 = numpy.dot(higher_moment_A, matrix_X) - e_k

    res = sum(e_k2)/n

    # Return result and time elapsed
    return res, '%.8e s' % (time.time() - start_time)
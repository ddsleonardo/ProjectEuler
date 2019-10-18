### https://www.projecteuler.net/problem=82

import sys
sys.path.append(r'..\euler')
import common as euler
import time

def read_file_as_matrix(path: str):
    ''' Reads a file with comma-separated numbers
    and returns the numbers in matrix form'''
    res = {}
    with open(path, 'r', newline='') as file:
        for index, line in enumerate(file):
            res[index] = [int(i) for i in line.split(',')]

    return res

def Problem82(path: str):
    ''' For a given matrix saved in .txt form,
    calculate the minimal path sum to cross the matrix
    following the rules laid out by the problem.'''

    # Initialise count and initial fraction
    start_time = time.time()

    # Read matrix from file
    # path_sum is where we'll store the min-cost to get to each cell
    # in a column. The first column comes straight from the original matrix
    matrix = read_file_as_matrix(path)
    path_sum = {}
    for row in matrix:
        path_sum[row] = [matrix[row][0]]

    for col in range(1, len(matrix[0])):
        for row in range(0, len(matrix)):
            # We go from left to right, top to bottom
            # for each new cell, the min cost before getting to it is either
            # the cell above or to the left
            if (row > 0):
                min_cost = min(path_sum[row][col - 1], path_sum[row - 1][col])
            else:
                min_cost = path_sum[row][col - 1]
            
            # Now we step down and check if actually coming up in the column
            # is the minimal cost path
            step = 1
            cost = 0
            while (row + step < len(matrix)):
                cost += matrix[row + step][col]
                if (cost + path_sum[row + step][col - 1] < min_cost):
                    min_cost = cost + path_sum[row + step][col - 1]
                
                step += 1

            path_sum[row].append(matrix[row][col] + min_cost)

    # The overall minimal cost will be the smallest value in the last column
    min_path_cost = min([path_sum[i][len(path_sum[i]) - 1] for i in range(len(path_sum))])

    # Return result and time elapsed
    return min_path_cost, '%.3f s' % (time.time() - start_time)
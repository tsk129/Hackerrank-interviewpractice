# Left Rotation

# A left rotation operation on an array of size  shifts each of the array's elements  unit to the left. Given an integer, , rotate the array that many steps left and return the result.

# Example


# After  rotations, .

# Function Description

# Complete the rotateLeft function in the editor below.

# rotateLeft has the following parameters:

# int d: the amount to rotate by
# int arr[n]: the array to rotate
# Returns

# int[n]: the rotated array
# Input Format

# The first line contains two space-separated integers that denote , the number of integers, and , the number of left rotations to perform.
# The second line contains  space-separated integers that describe .

# Constraints



import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    # Write your code here
    while d:
        arr.append(arr.pop(0))
        d -= 1
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

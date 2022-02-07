# 2D Array - DS

# Given a  2D Array, :

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# An hourglass in  is a subset of values with indices falling in this pattern in 's graphical representation:

# a b c
#   d
# e f g
# There are  hourglasses in . An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum. The array will always be .

# Example


# -9 -9 -9  1 1 1 
#  0 -9  0  4 3 2
# -9 -9 -9  1 2 3
#  0  0  8  6 6 0
#  0  0  0 -2 0 0
#  0  0  1  2 4 0
# The  hourglass sums are:

# -63, -34, -9, 12, 
# -10,   0, 28, 23, 
# -27, -11, -2, 10, 
#   9,  17, 25, 18
# The highest hourglass sum is  from the hourglass beginning at row , column :

# 0 4 3
#   1
# 8 6 6
# Note: If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.

# Function Description

# Complete the function hourglassSum in the editor below.

# hourglassSum has the following parameter(s):

# int arr[6][6]: an array of integers
# Returns

# int: the maximum hourglass sum
# Input Format

# Each of the  lines of inputs  contains  space-separated integers .

# Constraints

# Output Format

# Print the largest (maximum) hourglass sum found in .


import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    maxx = -9999999999
    def hgsum(arr,i,j):
        summ = 0
        for a in [i,i+2]:
            for b in range(j,j+3):
                summ += arr[a][b]
        return summ+arr[i+1][j+1]
    for i in range(4):
        for j in range(4):
            add = hgsum(arr,i,j)
            if add>maxx:
                maxx = add
    return maxx
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()



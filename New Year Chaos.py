# New Year Chaos

# It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from  to . Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.

# Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.

# Example


# If person  bribes person , the queue will look like this: . Only  bribe is required. Print 1.


# Person  had to bribe  people to get to the current position. Print Too chaotic.

# Function Description

# Complete the function minimumBribes in the editor below.

# minimumBribes has the following parameter(s):

# int q[n]: the positions of the people after all bribes
# Returns

# No value is returned. Print the minimum number of bribes necessary or Too chaotic if someone has bribed more than  people.
# Input Format

# The first line contains an integer , the number of test cases.

# Each of the next  pairs of lines are as follows:
# - The first line contains an integer , the number of people in the queue
# - The second line has  space-separated integers describing the final state of the queue.

# Constraints

# Subtasks

# For  score 
# For  score 


import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    b = 0
    Q = [i-1 for i in q]
    for i,j in enumerate(Q):
        if j-i > 2:
            print('Too chaotic')
            return
        for k in range(max(j-1, 0), i):
            if Q[k] > j:
                b += 1
    print(b)
            
        
    

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

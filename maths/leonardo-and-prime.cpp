#!/bin/python3

import os
import sys
pr=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
#
# Complete the primeCount function below.
#
def primeCount(n):
    #
    # Write your code here.
    #
    mul=pr[0]
    ans=0
    while  mul <= n:
        ans+=1
        mul*=pr[ans]
    return ans
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()


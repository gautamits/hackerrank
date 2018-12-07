#!/bin/python

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    problems = [range(1,n+1) for n in arr]
    pages=[]
    for i in problems:
        while len(i) > 0:
            pages.append(i[:k])
            i=i[k:]
    total=0
    result=[(j+1 in i) for (j,i) in enumerate(pages)]
    return sum(result)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = raw_input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = map(int, raw_input().rstrip().split())

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()


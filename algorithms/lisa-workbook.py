#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import count, zip_longest
# Complete the workbook function below.
def workbook(n, k, arr):
    page=count(1)
    return sum([len([1 for probs in zip_longest(*[iter(range(1, num_chpt_probs+1))]*k) if next(page) in probs]) for num_chpt_probs in arr])
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()


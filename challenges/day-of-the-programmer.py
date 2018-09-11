#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if year == 1918:
        return "26.09.1918"
    if year < 1918:
        return "%s.%s.%s" % (12 if year % 4 == 0 else 13,str(9).zfill(2),year)
    if year > 1918:
        return "%s.%s.%s" % (12 if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) else 13,str(9).zfill(2),year)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()


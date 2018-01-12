#!/bin/python

import sys

def marcsCakewalk(calorie):
    # Complete this function
    count=0
    s=0
    calorie=sorted(calorie)[::-1]
    for i in calorie:
        s+=2**count*i
        count+=1
    return s

if __name__ == "__main__":
    n = int(raw_input().strip())
    calorie = map(int, raw_input().strip().split(' '))
    result = marcsCakewalk(calorie)
    print result
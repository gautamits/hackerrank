#!/bin/python

import sys

def findMedian(arr):
    # Complete this function
    arr=sorted(arr)
    m=len(arr)/2
    return arr[m]

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    result = findMedian(arr)
    print result

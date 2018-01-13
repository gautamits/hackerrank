#!/bin/python

import sys

def chiefHopper(arr):
    # Complete this function
    ans=0
    for i in arr[::-1]:
        ans=(ans+i+1)/2
    return ans

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    result = chiefHopper(arr)
    print result

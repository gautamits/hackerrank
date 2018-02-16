#!/bin/python

import sys

def equalizeArray(arr):
    # Complete this function
    m={}
    for i in arr:
        try:
            m[i]+=1
        except:
            m[i]=1
    ma=m[arr[0]]
    for k in m:
        if m[k] > ma:
            ma=m[k]
    return len(arr)-ma

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    result = equalizeArray(arr)
    print result

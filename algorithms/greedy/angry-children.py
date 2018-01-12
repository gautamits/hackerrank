#!/bin/python

import sys

def angryChildren(k, arr):
    # Complete this function
    k-=1
    arr=sorted(arr)
    ans=arr[k]-arr[0]
    for i in range(k,len(arr)):
        if arr[i]-arr[i-k] < ans:
            ans=arr[i]-arr[i-k]
    return ans

if __name__ == "__main__":
    n = int(raw_input().strip())
    k = int(raw_input().strip())
    arr = []
    arr_i = 0
    for arr_i in xrange(n):
        arr_t = int(raw_input().strip())
        arr.append(arr_t)
    result = angryChildren(k, arr)
    print result

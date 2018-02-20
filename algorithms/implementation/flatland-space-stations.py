#!/bin/python3

import sys

def flatlandSpaceStations(n, c):
    # Complete this function
    arr=[100000]*n
    for i in c:
        arr[i]=0
    d=0
    #left traversal
    for i in range(min(c),n):
        if arr[i]!=0:
            arr[i]=d+1
            d+=1
        else:
            d=0
    #print(arr)
    #right traversal
    i=max(c)
    d=0
    while i >=0:
        if arr[i] > d+1:
            arr[i]=d+1
            d+=1
        else:
            d=0
        i-=1
    #print(arr)
    return max(arr)

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    c = list(map(int, input().strip().split(' ')))
    result = flatlandSpaceStations(n, c)
    print(result)

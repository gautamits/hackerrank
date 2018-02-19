#!/bin/python3

import sys

def stones(n, a, b):
    # Complete this function
    x=min(a,b)
    y=max(a,b)
    mi=0+(n-1)*x
    ma=0+(n-1)*y
    if mi==ma:
        return [mi]
    else:
        return range(mi,ma+1,y-x)

if __name__ == "__main__":
    T = int(input().strip())
    for a0 in range(T):
        n = int(input().strip())
        a = int(input().strip())
        b = int(input().strip())
        result = stones(n, a, b)
        print (" ".join(map(str, result)))
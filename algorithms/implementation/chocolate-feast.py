#!/bin/python3

import sys

def chocolateFeast(n, c, m):
    # Complete this function
    s=n//c
    wrappers=n//c
    while wrappers >= m:
        s+=wrappers//m
        wrappers=wrappers//m+wrappers%m
    return s
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n, c, m = input().strip().split(' ')
        n, c, m = [int(n), int(c), int(m)]
        result = chocolateFeast(n, c, m)
        print(result)

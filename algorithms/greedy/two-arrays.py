#!/bin/python

import sys

def twoArrays(k, A, B):
    # Complete this function
    result="YES"
    A=sorted(A)
    B=sorted(B)[::-1]
    for i,j in zip(A,B):
        if i+j < k:
            result="NO"
            break
    return result

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        n, k = raw_input().strip().split(' ')
        n, k = [int(n), int(k)]
        A = map(int, raw_input().strip().split(' '))
        B = map(int, raw_input().strip().split(' '))
        result = twoArrays(k, A, B)
        print result

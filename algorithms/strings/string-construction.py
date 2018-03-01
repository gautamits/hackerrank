#!/bin/python3

import sys

def stringConstruction(s):
    # Complete this function
    S=set()
    ans=0
    for i in s:
        if i in S:
            continue
        else:
            ans+=1
            S.add(i)
    return ans

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = stringConstruction(s)
        print(result)

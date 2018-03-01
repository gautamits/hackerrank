#!/bin/python3

import sys

def gameOfThrones(s):
    # Complete this function
    m={}
    for i in s:
        try:
            m[i]+=1
        except:
            m[i]=1
    odd=0
    for i in m:
        if m[i]%2==1:
            odd+=1
    if odd > 1:
        return 'NO'
    else:
        return 'YES'

s = input().strip()
result = gameOfThrones(s)
print(result)

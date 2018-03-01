#!/bin/python3

import sys

def funnyString(s):
    # Complete this function
    i=0
    n=len(s)-1
    temp=n/2;
    while i <= temp and n >= temp:
        if abs(ord(s[i+1])-ord(s[i])) == abs(ord(s[n])-ord(s[n-1])):
            i+=1
            n-=1
            continue
        else:
            return "Not Funny"
    return "Funny"

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = funnyString(s)
    print(result)


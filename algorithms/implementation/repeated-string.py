#!/bin/python

import sys

def repeatedString(s, n):
    # Complete this function
    count=0
    for i in s:
        if i=='a':
            count+=1
    res=count*(n/len(s))
    for i in s[:n%(len(s))]:
        if i=='a':
            res+=1
    return res

if __name__ == "__main__":
    s = raw_input().strip()
    n = long(raw_input().strip())
    result = repeatedString(s, n)
    print result

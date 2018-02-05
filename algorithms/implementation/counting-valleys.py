#!/bin/python3

import sys

def countingValleys(n, s):
    # Complete this function
    height=0
    ans=0
    for i in s:
        if i=='U':
            height+=1
        else:
            height-=1
        if height==0 and i=='U':
            ans+=1
    return ans
            
            
            

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    result = countingValleys(n, s)
    print(result)

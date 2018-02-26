#!/bin/python3

import sys

def hackerrankInString(s):
    # Complete this function
    m={}
    j=0
    ans=""
    for i in 'hackerrank':
        while j < len(s) and s[j] != i :
            j+=1
        try:
            ans+=s[j]
            j+=1
        except:
            pass
    if ans=='hackerrank':
        return 'YES'
    else:
        return 'NO'
    
        
        

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = hackerrankInString(s)
        print(result)

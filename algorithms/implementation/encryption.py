#!/bin/python3

import sys
from math import ceil, floor, sqrt

def encryption(s):
    # Complete this function
    s=s.replace(" ","")
    row=int(floor(sqrt(len(s))))
    column=int(ceil(sqrt(len(s))))
    arr=[]
    while len(s)>column:
        arr.append(list(s[:column]))
        s=s[column:]
    if len(s) > 0:
        arr.append(s)
    arr[-1]=arr[-1]+(column-len(arr[-1]))*" "
    arr[-1]=list(arr[-1])
    arr=list(zip(*arr))
    
    arr=["".join(i) for i in arr]
    arr=[i.replace(" ","") for i in arr]
    return " ".join(arr)
    
                
    
    

if __name__ == "__main__":
    s = input().strip()
    result = encryption(s)
    print(result)


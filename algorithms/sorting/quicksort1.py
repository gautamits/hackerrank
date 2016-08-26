#!/bin/python
def partition(ar): 
    left=[]
    right=[]
    equal=[]
    key=ar[0]
    for i in ar:
        if i > key:
            right.append(i)
        elif i < key:
            left.append(i)
        else:
            equal.append(i)
    arr=left+equal+right
    print " ".join(map(str,arr))
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)

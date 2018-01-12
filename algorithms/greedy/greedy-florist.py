#!/bin/python

import sys

def getMinimumCost(n, k, c):
    # Complete this function
    persons=[0]*k
    items=[0]*k
    c=sorted(c)[::-1]
    for i in c:
        #print i,
        minindex=items.index(min(items))
        items[minindex]=items[minindex]+1
        persons[minindex]+=(items[minindex])*i
        #print persons
        #print items
        
    #print persons
    return sum(persons)

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
c = map(int, raw_input().strip().split(' '))
minimumCost = getMinimumCost(n, k, c)
print(minimumCost)

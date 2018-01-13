#!/bin/python

import sys

def boardCutting(cost_y, cost_x):
    # Complete this function
    arr=[]
    for i in cost_y:
        arr.append((i,2))
    for i in cost_x:
        arr.append((i,1))
    arr=sorted(arr)[::-1]
    #print arr
    vertical=0
    horizontal=0
    ans=0
    
    for i in arr:
        if i[1]==2:
            ans=ans+(horizontal+1)*i[0]
            vertical+=1
        else:
            ans=ans+(vertical+1)*i[0]
            horizontal+=1
    return ans

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        m, n = raw_input().strip().split(' ')
        m, n = [int(m), int(n)]
        cost_y = map(int, raw_input().strip().split(' '))
        cost_x = map(int, raw_input().strip().split(' '))
        result = boardCutting(cost_y, cost_x)
        print result%1000000007

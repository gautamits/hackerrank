#!/bin/python

import sys

def maximumToys(prices, k):
    # Complete this function
    prices=sorted(prices)
    s=0
    for i in range(len(prices)):
        s+=prices[i]
        if s>k:
            return i
        

if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    prices = map(int, raw_input().strip().split(' '))
    result = maximumToys(prices, k)
    print result

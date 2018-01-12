#!/bin/python

import sys

def toys(w):
    # Complete this function
    w=sorted(w)
    units=1
    weight=w[0]
    for index in range(len(w)):
        if w[index] <= weight+4:
            pass
        else:
            units+=1
            weight=w[index]
    return units

if __name__ == "__main__":
    n = int(raw_input().strip())
    w = map(int, raw_input().strip().split(' '))
    result = toys(w)
    print result

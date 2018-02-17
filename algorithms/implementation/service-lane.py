#!/bin/python

import sys

def serviceLane(width, cases):
    # Complete this function
    for i,j in cases:
        yield min(width[i:j+1])

if __name__ == "__main__":
    n, t = raw_input().strip().split(' ')
    n, t = [int(n), int(t)]
    width = map(int, raw_input().strip().split(' '))
    cases = []
    for cases_i in xrange(t):
        cases_temp = map(int,raw_input().strip().split(' '))
        cases.append(cases_temp)
    result = serviceLane(width, cases)
    print "\n".join(map(str, result))

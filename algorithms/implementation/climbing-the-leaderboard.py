#!/bin/python

import sys

def climbingLeaderboard(scores, alice):
    # Complete this function
    scores=sorted(set(scores),reverse=True)
    l = len(scores)

    for a in alice:
        while (l > 0) and (a >= scores[l-1]):
            l -= 1
        yield l+1

if __name__ == "__main__":
    n = int(raw_input().strip())
    scores = map(int, raw_input().strip().split(' '))
    m = int(raw_input().strip())
    alice = map(int, raw_input().strip().split(' '))
    result = climbingLeaderboard(scores, alice)
    print "\n".join(map(str, result))
#!/bin/python

import sys

def gridChallenge(grid):
    # Complete this function
    ans="YES"
    for i in range(len(grid)):
        grid[i]=sorted(grid[i])
    for i in range(len(grid)):
        for j in range(1,len(grid)):
            if grid[j][i] < grid[j-1][i]:
                ans="NO"
                break
    return ans

if __name__ == "__main__":
    t = int(raw_input().strip())
    for _ in range(t):
        n = int(raw_input().strip())
        grid = []
        grid_i = 0
        for grid_i in xrange(n):
            grid_t = str(raw_input().strip())
            grid.append(grid_t)
        result = gridChallenge(grid)
        print result

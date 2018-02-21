#!/bin/python3

import sys

def cavityMap(grid):
    # Complete this function
    for i in range(1,len(grid)-1):
        for j in range(1,len(grid[i])-1):
            if grid[i][j] > max([grid[i+1][j], grid[i-1][j], 
grid[i][j+1], grid[i][j-1]]):
                grid[i][j]='X'
    for i in range(len(grid)):
        grid[i]="".join(grid[i])
    return grid

if __name__ == "__main__":
    n = int(input().strip())
    grid = []
    grid_i = 0
    for grid_i in range(n):
       grid_t = list(input())
       grid.append(grid_t)
    result = cavityMap(grid)
    print ("\n".join(map(str, result)))


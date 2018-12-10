#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    n = len(grid)
    grid_list = list(grid)
    for i in range(1, n-1):
        for j in range(1, n-1):
            if grid_list[i][j]>grid_list[i][j-1] and grid_list[i][j]>grid_list[i][j+1] \
            and grid_list[i][j]>grid_list[i-1][j] and grid_list[i][j]>grid_list[i+1][j]:
                grid_list[i] = str(grid_list[i][:j]) + 'X' + str(grid_list[i][j+1: ]) 
    
    
    return grid_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

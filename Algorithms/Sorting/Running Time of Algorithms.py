#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(arr):
    s = 0
    l = { i:x for i,x in enumerate(arr)}
    for i in range(2,len(arr)+1):
        x = sorted(arr[:i])
        _max = float("-inf")
        _min = float("inf")
        c = False
        for j,n in enumerate(x):
            if l[j] != n:
                _max = max(_max,j)
                _min = min(_min,j)
                l[j] = n
                c = True
        if c:
            s += _max - _min
        arr[:i] = x
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

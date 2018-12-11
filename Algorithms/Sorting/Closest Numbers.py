#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort()
    minc=math.inf
    l=[]
    for i in range(len(arr)-1):
        if(abs(arr[i]-arr[i+1]) < minc):
            minc=abs(arr[i]-arr[i+1])
    for i in range(len(arr)-1):
        if(abs(arr[i]-arr[i+1]) == minc):
            if(arr[i]<arr[i+1]):
                l.append(arr[i])
                l.append(arr[i+1])
            else:
                l.append(arr[i+1])
                l.append(arr[i])
    return l

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

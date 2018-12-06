#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    lst = []
    mini = 0
    maxi = 0
    lst.append(scores[0])
    for x in scores:
        if x<min(lst):
            mini+=1
        if x>max(lst):
            maxi+=1
        lst.append(x)
    return [maxi,mini]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    # Time : O(N log N)
    # Space : O(N)
    # Method : sort the frequency values of characters and try decrementing the last element
    d = {}
    for l in s:
        if l in d.keys():
            d[l] += 1
        else:
            d[l] = 1
    
    f = sorted(d.values())
    decision = "NO"
    print(f)
    if len(set(f)) == 1:
        decision = "YES"
    else:
        if (f[0]- 1 == 0):
            f.pop(0)
        elif (f[-1] - 1 == f[-2]):
            f[-1] -= 1
        if len(set(f)) == 1:
            decision = "YES"
            
    return decision

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

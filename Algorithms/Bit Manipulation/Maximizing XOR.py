#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations, starmap
from operator import xor

# Complete the maximizingXor function below.
def maximizingXor(l, r):
    return max(starmap(xor, combinations(range(l,r+1),2)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input())

    r = int(input())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()

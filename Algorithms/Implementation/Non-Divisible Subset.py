#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the nonDivisibleSubset function below.
def nonDivisibleSubset(k, S):
    remainder_array = [i % k for i in S]
    check_array = []
    for i in set(remainder_array):
        if k-i not in check_array:
            check_array.append(i)
    return sum([1 if i==0 or i*2==k else max(remainder_array.count(i), remainder_array.count(k-i)) for i in check_array])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    S = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, S)

    fptr.write(str(result) + '\n')

    fptr.close()

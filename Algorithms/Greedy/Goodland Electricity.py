#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pylons function below.
def pylons(k, arr):
    ret = 0
    i = k-1
    i_pre = -1
    n = len(arr)

    while i<n:
        passed = False
        if arr[i] == 1:
            ret += 1
            i_pre = i
            if (i+(2*k)-1)<n:
                i += (2*k)-1
            elif (i+k) < n:
                i = n-1
            else:
                return ret
            continue
        else:
            for j in range(1, 2*k-1):
                if (i-j) > i_pre:
                    if arr[i - j] == 1:
                        ret += 1
                        passed = True
                        i_pre = i
                        if ((i-j)+(2*k)-1) < n:
                            i = (i-j)+(2*k)-1
                        elif (i-j)+k < n:
                            i = n-1
                        else:
                            return ret
                        break
                else:
                    break
            if not passed:
                return -1
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sansaXor function below.
def sansaXor(arr):
    res=0
    arr_len=len(arr)
    j=1
    for i in range(len(arr)):
        if j*(arr_len)%2==1:
            res^=arr[i]
        j+=1
        arr_len-=1
    return res
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)

        fptr.write(str(result) + '\n')

    fptr.close()

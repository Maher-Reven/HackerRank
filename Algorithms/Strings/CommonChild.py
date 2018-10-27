#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2):
    n = len(s1)        
    m = len(s2)        
    CCi = [0] * (m + 1)
    CCj = [0] * (m + 1)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                CCj[j] = CCi[j - 1] + 1
            elif CCi[j] > CCj[j - 1]:
                CCj[j] = CCi[j]
            else:
                CCj[j] = CCj[j - 1]
        CCi = CCj
        CCj = [0] * (m + 1)
    return CCi[-1] 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    sev = 0
    vad = 0
    pre = 0
    for element in s:
        if(sev<0):
            pre = 1
        if(sev>=0):
            pre = 0
        if(element=='U'):
            sev+=1
        elif(element=='D'):
            sev-=1
        if((sev==0)and (pre==1)):
            vad+=1
    return(vad)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

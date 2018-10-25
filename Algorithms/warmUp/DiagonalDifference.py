#!/bin/python3
'''
25 OCT, 2018
@author: Graves88si(Maher Krde)
'''

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
n = int(input().strip())
dSumLeft  = 0
dSumRight  = 0
for i in range(n):
    matrixRow = list(map(int,input().strip().split(' ')))
    dSumLeft += int(matrixRow[i])
    dSumRight += int(matrixRow[n-i-1])
print(abs(dSumLeft - dSumRight))

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    return 'YES' if sum([1 for i in "abcdefghjkilmnopqrstuvwxyz" if i in s if sum([1 for j in s if i==j])%2==1]) <=1 else 'NO'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()

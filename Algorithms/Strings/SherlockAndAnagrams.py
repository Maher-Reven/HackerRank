#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    count=0
    dict={}
    n=len(s)
    for i in range(n):
        for j in range(n-i):
            sub=''.join(sorted(s[j:j+i+1]))
            try:
                dict[sub]+=1
            except:
                dict[sub]=1
    for i in dict:
        count+=dict[i]*(dict[i]-1)//2
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

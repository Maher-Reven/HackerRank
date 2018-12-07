import math
import os
import random
import re
import sys

# Complete the serviceLane function below.
def serviceLane(n, cases):
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))
   

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    #result = serviceLane(n, cases)
    result=[]
    for case in cases:
        start_index = case[0]
        end_index = case[1] + 1
        result.append(min(width[start_index:end_index]))
    

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
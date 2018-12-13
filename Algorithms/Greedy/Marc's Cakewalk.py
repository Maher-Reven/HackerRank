input()
print(sum(c * 2 ** j for (j, c) in enumerate(sorted(map(int, input().split()), reverse=True))))



#2nd solution py3 
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marcsCakewalk function below.
def marcsCakewalk(calorie):
    sum=0
    calorie.sort(reverse=True)
    for i in range(len(calorie)):
        sum+=pow(2,i)*calorie[i]
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()

i, j, k = [int(x) for x in input().split()]
beautifulDays = [1 for day in range(i, j+1) if (day - int(str(day)[::-1])) % k == 0]
print(sum(beautifulDays))




#2nd solution 

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# # Complete the beautifulDays function below.
# def beautifulDays(i, j, k):
#     return len([ x for x in range(i,j+1) if abs(x - int(str(x)[::-1].lstrip("0"))) % k == 0 ])

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     ijk = input().split()

#     i = int(ijk[0])

#     j = int(ijk[1])

#     k = int(ijk[2])

#     result = beautifulDays(i, j, k)

#     fptr.write(str(result) + '\n')

#     fptr.close()

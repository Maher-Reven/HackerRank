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

N = int(input().strip())
print('Weird' if N % 2 !=0 or 6<=N<=20 else "Not Weird")

#2nd solution
# N = int(input().strip())

# ans = 'Weird'

# if N % 2 == 0 and not 6 <= N <= 20:
#     ans = 'Not ' + ans
    
# print(ans)
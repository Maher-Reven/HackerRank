#!/bin/python3
'''
24 OCT, 2018
@author: Graves88si(Maher Krde)
'''

import os
import sys
def simpleArraySum(ar):
    return sum(ar)
ar_count = int(input())
ar = list(map(int, input().rstrip().split()))
result = simpleArraySum(ar)
print(result)



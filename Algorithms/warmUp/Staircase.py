#!/bin/python3
'''
26 OCT, 2018
@author: Graves88si(Maher Krde)
'''

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(a):
    for i in range(1, a + 1):
        print((a - i) * ' ' + i * "#")


n = int(input())
staircase(n)
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    ar=[]
    ar1=[]
    for i in range(0,32)    :
        ar.append(0)
        ar1.append(1)
    i=0
    while(n!=0) :
        d= n%2
        n= n//2
        ar[31-i]= d
        ar1[31-i]= ar1[31-i]-d
        i+= 1
    print(ar)
    print(ar1)
    add= 0
    for i in range(0,32)    :
        add+= ar1[i] * math.pow(2,31-i)
    return(int(add))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

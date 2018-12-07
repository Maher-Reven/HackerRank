#!/bin/python3
import sys

function = lambda n,c,m: n//c + 1/(m-1) * (n/c) - 1/(m-1)
t = int(input().strip())
for a0 in range(t):
    n,c,m = input().strip().split(' ')
    n,c,m =[int(n),int(c),int(m)]
    print(int(function(n,c,m)))


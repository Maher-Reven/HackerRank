#!/bin/python2
def partition(ar):
    p=ar[0]
    eq,left,right=[],[],[]
    for i in ar:
        if i >= p:
            right.append(i)
        elif i <p:
            left.append(i)
    for t in left:
        print t,  
    for k in right:
        print k,
        
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)


#2nd solution py3
from itertools import chain

n = int(input())
p, *a = map(int, input().split())
first, equal, last = [], [p], []
for i in a:
    if i < p:
        first.append(i)
    elif i > p:
        last.append(i)
    else:
        equal.append(i)
print(*chain(first, equal, last))


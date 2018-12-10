#!/bin/python3

import sys
import math


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
c.sort()
global_max=0
L=len(c)
for i in range(0,L+1):
    if(i==0):
        local_max=c[i]-0
    elif(i==L):
        local_max=(n-1)-c[L-1]
    elif(c[i]-c[i-1] >1):
        local_max=math.floor((c[i]-c[i-1])/2)
    if(local_max>global_max):
        global_max=local_max
  
        
    
            
print(global_max)s
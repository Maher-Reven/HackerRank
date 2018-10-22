'''
Oct 22, 2018
@author : Graves88si(Maher Krde)
'''

import numpy as np
from collections import Counter



n=int(input())
number=[int(x) for x in input().split()]
print(round(np.mean(number),1))
print(round(np.median(number),1))
freq=Counter(number)
mode=max(freq.values())
x=[]
for key,value in freq.items():
    if value==mode:
        x.append(key)
        
result=sorted(list(set(x)))
print(result[0])
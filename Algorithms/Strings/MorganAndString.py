#!/bin/python3
'''
26 OCT, 2018
@author: Graves88si(Maher Krde)
'''

for i in range(int(input())):
    s1 = input().strip()
    s2 = input().strip()
    len1 = len(s1)
    len2 = len(s2)
    i, j = 0,0
    output = []
    while (i <= len1 - 1)  and (j <= len2 - 1):
        if s1[i:-1] < s2[j:-1]:            
            output.append(s1[i])
            i += 1
        else:
            output += s2[j]
            j += 1
    if i == len1:
        output.append(s2[j:])
    if j == len2:
        output.append(s1[i:])
    
    print("".join(output))
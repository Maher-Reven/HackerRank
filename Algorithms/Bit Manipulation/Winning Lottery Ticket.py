#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the winningLotteryTicket function below.
def winningLotteryTicket(tickets):
    s=set(list(map(str,range(0,10))))
    lst=[]
    for i in range(0,len(tickets)):
        for j in range(i+1,len(tickets)):
            if set(str(tickets[i])).union(set(str(tickets[j]))).issuperset(s):
                lst.append((tickets[i],tickets[j]))  
    return len(lst)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    tickets = []

    for _ in range(n):
        tickets_item = input()
        tickets.append(tickets_item)

    result = winningLotteryTicket(tickets)

    fptr.write(str(result) + '\n')

    fptr.close()

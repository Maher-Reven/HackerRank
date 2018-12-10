#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridSearch function below.
def gridSearch(G, P):

    for row_num in range(0, len(G)):
        if P[0] in G[row_num]:
            current_idx = G[row_num].index(P[0])
            lst_idx = []
            while current_idx <= len(G[0]):
                next_idx = G[row_num].find(P[0],current_idx)
                if next_idx != -1:
                    lst_idx.append(next_idx)
                    current_idx = next_idx + 1
                else:
                    break


            for idx in lst_idx:
                p_match = []
                for y in range(0, len(P)):
                    p_match.append(G[row_num+y][idx:idx+len(P[0])])

                if p_match == P:
                    return 'YES'

    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()

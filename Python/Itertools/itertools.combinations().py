from itertools import combinations as com

s , n  = input().split()

for i in range(1, int(n)+1):
    for j in com(sorted(s), i):
        print (''.join(j))
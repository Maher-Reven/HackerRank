from itertools import combinations_with_replacement as com

s, k = input().split()

for c in com(sorted(s), int(k)):
    print("".join(c))
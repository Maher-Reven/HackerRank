from itertools import permutations as p
s,n = input().split()
print(*[''.join(i) for i in p(sorted(s),int(n))],sep='\n')
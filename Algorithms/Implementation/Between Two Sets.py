
import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]
a.sort()
b.sort()
ausgabe = 0
for q in range(b[0] +1):
    if q >= a[-1]:
        for t in range(n):
            if q % a[t] != 0:
                break
            if t == n -1:
                for g in range(m):
                    if b[g] % q != 0:
                        break
                    if g == m -1:
                        ausgabe += 1
      
print(ausgabe)
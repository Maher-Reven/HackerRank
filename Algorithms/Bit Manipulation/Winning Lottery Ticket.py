from itertools import combinations
import math

if __name__ == "__main__":
    k = [sum(2**(ord(i)-48) for i in ''.join(set(s))) for s in [input() for x in range(int(input()))]]
    c = combinations(list(enumerate([k.count(x) for x in range(1024)])), 2)
    n = sum(x[0][1] * x[1][1] for x in c if (x[0][0] | x[1][0] == 1023) and x[0][1] > 0 and x[1][1] > 0)
    inner = max(0, k.count(1023)-1)
    print(n + (inner * inner + inner)//2)
from numpy import array
n, _m = map(int, input().split())
a = array([input().split() for _ in range(n)], int)
print(a.min(axis=1).max())

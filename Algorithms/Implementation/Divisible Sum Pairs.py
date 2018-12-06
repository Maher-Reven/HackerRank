n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = [[c, d] for x, c in enumerate(a) for y, d in enumerate(a) if x < y and (c + d) % k == 0]
print(len(b))
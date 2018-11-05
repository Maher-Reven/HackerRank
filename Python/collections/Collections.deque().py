from collections import deque
que = deque()
for _ in range(int(input())):
    method, _, args = input().strip().partition(" ")
    getattr(que, method)(*args.split())
print(*list(que))
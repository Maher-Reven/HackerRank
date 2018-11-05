import numpy as np
np.set_printoptions(legacy='1.13')

r, c = list(map(int, input().split()))
data = []
for _ in range(r):
    data.append(list(map(int, input().split())))
    
print(np.mean(data, axis=1))
print(np.var(data, axis=0))
print(np.std(data))

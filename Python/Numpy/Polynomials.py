import numpy as np 
a = [float(_) for _ in input().split()]
x = float(input())
print(np.polyval(a, x))




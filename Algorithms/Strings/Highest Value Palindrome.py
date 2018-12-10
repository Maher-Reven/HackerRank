x,y = [int(t) for t in input().split()]
k = input()
v = [int(h) for h in k]
n = len(k) 

r,z,c = 1,n//2,[0]*n

for i in range(z):
    if v[i] != v[n-i-1]:
        if y <= 0:
            r = -1
            break
        y = y - 1
        if v[i] > v[n-i-1]:
            v[n-i-1],c[n-i-1] = v[i],-1
        else:
            v[i],c[i] = v[n-i-1],-1

if y > 0:
    for j in range(z):
        if y <= 0:
            break
        if c[j] == -1 or c[n-j-1] == -1:
            if v[j] != 9:
                v[j], v[n-j-1],y = 9, 9,y-1
        else:
            if v[j] != 9:
                if y > 1:
                    v[j], v[n-j-1] = 9, 9
                    y = y - 2
    if n % 2 == 1 and y > 0:
        v[z] = 9
            
if r != -1:
    print(''.join([str(h) for h in v]))
else:
    print(r)
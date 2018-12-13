#py2

a = map(int,raw_input().strip().split(' '))
a1,a2,n=a[0],a[1],a[2]
a=[]
def fib(n):
    if n==1:
        a.append(a1)
    elif n==2:
        a.append(a2)
    else:
        a.append(a[n-2]*a[n-2]+a[n-3])
i=1
while i<=n:
    fib(i)
    i+=1
print a[n-1]
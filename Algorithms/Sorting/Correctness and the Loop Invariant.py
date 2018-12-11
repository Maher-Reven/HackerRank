n=int(input())
l=list(map(int,input().split()))
l.sort()
print(*l)

#2nd solution also py3
n,m=input(),list(map(int, input().strip().split()))
m.sort()
print(*m, sep=" ")

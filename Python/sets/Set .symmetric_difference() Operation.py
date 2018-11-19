n,s1=int(input()),set(map(int,input().split()))
b,s2=int(input()),set(map(int,input().split()))
print(len((s1.difference(s2)).union(s2.difference(s1))))
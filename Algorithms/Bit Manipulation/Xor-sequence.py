def xorSum(n):
    return([n,n,2,2,n+2,n+2,0,0][n%8])
for _ in range(int(input())):
    l,r=map(int,input().strip().split())
    print(xorSum(l-1)^xorSum(r))
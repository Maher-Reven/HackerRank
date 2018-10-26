n,m=map(int,input().split())
arr = map(int,input().split())
a=set(map(int,input().split()))
b=set(map(int,input().split()))
maher=0
for i in arr:
    if i in a:
        maher +=1
    if i in b:
        maher -=1
print(maher)            

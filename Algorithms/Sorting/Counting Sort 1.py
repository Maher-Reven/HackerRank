n = int(input())
l = [0]*100
for i in map(int,input().split()):
    l[i]+=1
print(*l)



#2nd solution
n=int(input())
l=list(map(int,input().split()))
u=[0]*100   #all zeros list of size 100
for i in l:
    u[i]+=1
for i in u:
    print(i,end=" ")
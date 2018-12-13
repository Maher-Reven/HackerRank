import itertools

n=int(input().strip())
arr= input().strip().split()
arr=[int(i) for i in arr]

perms = list(itertools.permutations(arr, n))

prev=0
p=[]

for i in perms:
    high=0
    count=0
    i=list(i)
    #print(i)
    for j in i:
        if count==0:
            prev=j
        else:
            #print(prev,j,prev^j)
            if (prev^j)>high:
                high=prev^j
            prev=j
        count=count+1
    #print(high)
    p.append(high)
        
print(min(p))
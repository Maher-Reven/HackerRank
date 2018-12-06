n=int(input())
ar=[int(x) for x in input().split()]
countList=[]
for i in ar:
    countList.append(ar.count(i))
max_c=max(countList)
i=0
result=[]
while i<len(countList):
    if countList[i]==max_c:
        result.append(ar[i])
    i+=1
print(min(result))
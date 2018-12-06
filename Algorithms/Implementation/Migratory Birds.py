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



#2nd solution

raw_input()
types = map(int, raw_input().split())

bird_count = {}

for typ in types:
    bird_count[typ] = bird_count.get(typ, 0) + 1
    
print max(bird_count, key=lambda x: bird_count[x])
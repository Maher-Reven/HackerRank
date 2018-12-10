import sys

altered=0
inp = input().strip()
for i in range(len(inp)):
    x=i%3
    if(x==0 and inp[i]!='S'):
        altered+=1
    elif(x==1 and inp[i]!='O'):
        altered+=1
    elif(x==2 and inp[i]!='S'):
        altered+=1
print(altered)
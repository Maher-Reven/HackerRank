'''
Oct 22, 2018
@author : Graves88si(Maher Krde)
'''
n=int(input())
num=[int(x) for x in input().split()]
weight=[int(x) for x in input().split()]
p=0
for i,j in zip(num,weight):
    p+=i*j
result=round(p/sum(weight),1)
print(result)
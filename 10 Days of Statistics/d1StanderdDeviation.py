'''
Oct 24, 2018
@author : Graves88si(Maher Krde)
'''

n=int(input())
num=[int(x) for x in input().split()]
mean=sum(num)/n
var=0
for i in num:
    var+=(i-mean)**2
var=var/n
std=round(var**0.5,1)
print(std)


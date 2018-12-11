v, n = input(), input()
print(input().split().index(v))



#2nd solution py2
v = int(input())
n = int(input())
print map(int,raw_input().strip().split(" ")).index(v)



#3rd solution py3 with eval
p=eval(input())
n=eval(input())
lis=[int(x) for x in input().split()]
print(lis.index(p))


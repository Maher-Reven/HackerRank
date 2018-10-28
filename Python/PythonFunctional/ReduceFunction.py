from fractions import Fraction
from functools import reduce
from fractions import Fraction
from functools import reduce
l=[]
for _ in range(int(input())):
    a,b=input().split() 
    c=Fraction(int(a),int(b))
    l.append(c)
print(str(reduce(lambda x,y: x*y,l).numerator)+" "+str(reduce(lambda x,y: x*y,l).denominator))

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
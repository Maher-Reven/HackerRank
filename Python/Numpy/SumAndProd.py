import numpy
f = []
input()
while True:
    try:
        o = [ int(x) for x in input().split(' ')]
        f.append(o)
    except:
        break
f = numpy.array(f)
s = f.sum(axis = 0)
print(s.prod(axis = 0))a
import numpy

A, B = [numpy.array(raw_input().split(), int) for _ in range(2)]
print '\n'.join(str(op(A, B)) for op in (numpy.inner, numpy.outer))
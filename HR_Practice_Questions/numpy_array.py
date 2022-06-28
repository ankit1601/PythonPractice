import numpy

def arrays(arr):
    return numpy.array(arr[::-1], float)
    # complete this function
    # use numpy.array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

import numpy
arr = list(map(int, input().split()))
a = numpy.array(arr)
a.shape = (3,3)
print(a)

import numpy
m, n = list(map(int, input().split()))
a = numpy.array([input().strip().split() for _ in range(n)], int)
print(a.transpose())
print(a.flatten())


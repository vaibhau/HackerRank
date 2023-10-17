# Solution 1

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    return numpy.array(arr,float)[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# Solution 2

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr.reverse()
    return numpy.array(arr,float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

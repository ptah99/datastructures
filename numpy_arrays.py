# proving that numpy arrays take less time
import numpy as np
import time
import sys

SIZE = 1000000

L1 = range(SIZE)
L2 = range(SIZE)

A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

start = time.time()
result = [(x, y) for x, y in zip(L1, L2)]
# print((time.time()-start)*1000)

start = time.time()
result = A1 + A2
# print((time.time()-start)*1000)

# NUMPY OPERATIONS
a = np.array([(1, 2, 3), (2, 4, 3)])
print(a.ndim)  # to know if it is a two dimensional array
print(a.itemsize)  # byte size of each element
print(a.dtype)  # data type stored
print(a.size)  # size of array
print(a.shape)

r = np.array([(1, 2, 3, 4), (3, 4, 5, 6)])
# r = r.reshape(4,2)
print(r)
print(a[0, 2])  # slicing a[0:,3]
l = np.linspace(1, 3, 5)
print(l)
print(r.max())
print(r.sum(axis=0))
# square root of each element and std dev
print(np.sqrt(r))
print(np.std(r))

#  matrix wise operations
y = np.array([(1, 2, 3, 4), (3, 4, 5, 6)])
print(r + y)
print(r * y)

# concatenate
print(np.hstack((r, y)))  # vstack
# convert array to single
print(r.ravel())

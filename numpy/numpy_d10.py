#
# Day 10
#

import numpy as np

#

a = np.array([1, 2, 3], dtype='int16')
b= np.array([[9.0, 8.0, 5.0], [6.0, 5.0, 4.0]])

# Get dimension
print(f'\nDimension: {b.ndim}') # --> 2 because it's two lists

# Get shape
print(f'Shape: {b.shape}') # --> (2, 3) because it's 2 lists containing 3 values (size 3)

# Get type
print(f'Array "a" type: {a.dtype}') # --> int16
print(f'Array "b" type: {b.dtype}') # --> float64

# Get size
print(f'Array "a" size: {a.itemsize}')

# Get total size
print(f'Total size array "a": {a.size * a.itemsize}')
print(f'Total size array "a": {a.nbytes}') # --> array.nbytes == array.size * array.itemsize
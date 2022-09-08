#
# Day 10
#

import numpy as np

### --> The basics

def basics():
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

### --> Accessing / changing elements (slicing)

def slicing():
    a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])

    # Get specific element [row, column]
    print(f'6th element in the 2nd row: {a[1, 5]}') # --> Works the same as with lists, with negative indices

    # Get a specific row
    print(f'Get all the first row: {a[0, :]}')

    # Get a specific column
    print(f'Get all the 5th indices: {a[:, 5]}')

    # Getting fancy with slicing
    print(f'Get every 3rd item in the 2nd row: {a[1, 0::3]}') # Slice properties --> array[row, column _startindex:endindex:step]

    # Change an item
    a[1, 0] = 16
    print(f'New value: {a[1, 0]}')

    # Change all items in a column:
    a[:, 6] = 0
    print(f'Array with new values:\n{a}')

    # Work with 3-D array
    b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    print(f'3-D array:\n{b}')
    # Get specific element (work outside --> in)
    print(f'First set, second row, second item: {b[0, 1, 1]}')
    print(f'Get every first item from every row in all sets:\n{b[:, :, 0]}')

    # Replace in 3-D array
    b[:, :, 1] = -1
    print(f'Replace all second values in every row and array:\n{b}')

### Initializing different arrays

def initializing_diff_arrays():
    # All 0s matrix --> np.zeros()
    print(f'5 sets of 1 row and 5 items:\n{np.zeros((5, 1, 5))}')

    # all 1s matrix --> np.ones()
    print(f'3 sets of 3 rows and 3 items:\n{np.ones((3, 3, 3))}')

    # Any other matrix --> np.full()
    print(f'2 sets of 2 row and 10 items:\n{np.full((2, 2, 10), -1)}')

    # Random decimal numbers
    print(np.random.rand(4, 2))

    # Random integer values --> np.random.randint(startvalue, endvalue, size=(array, size))
    print(np.random.randint(-10, 10, size=(2, 10)))

    # Identity matrix
    print(np.identity(10))

    # Repeat an array --> np.repeat(a=array, repeats=times_repeated, axis=(1, 0))
    arr = np.array([[1, 2, 3, 4]])
    r1 = np.repeat(arr, 3, axis=0)
    print(r1)

### Problem #1

def my_solution():
    cube = np.array([np.zeros(5)], dtype='int16').repeat(5, axis=0)
    cube[:, 0:5:4] = np.ones(1)
    cube[0:5:4, :] = np.ones(1)
    cube[2, 2] = np.full(1, 9)
    print(cube)

def freeCodeCampSolution():
    output = np.ones((5, 5))
    z = np.zeros((3, 3))
    z[1, 1] = 9
    output[1:-1, 1:-1] = z
    print(output)

### Mathematics

def np_math():
    a = np.array([1, 2, 3, 4])

    # Addition --> Adds the number specified to each item of the array
    print(a + 2)

    # Subtract --> Subtracts the number specified to each item of the array
    print(a - 2)

    # Multiplication --> Multiplies by the number specified each item of the array
    print(a * 2)

    # Division --> Divides each item of the array by the number specified
    print(a / 2)

    # Get sin(), cos(), tan() values of each item
    print(f'Sin: {np.sin(a)}\nCosin: {np.cos(a)}\nTangens: {np.tan(a)}')

### Statistics

def np_statistics():
    stats = np.array([[1, 2, 3],[4, 5, 6]])

    # Minimum/Maximum value
    print(f'{np.min(stats)}\t{np.max(stats)}')

    # Minimum/Maximum value per-row in a multi-row array
    print(f'{np.min(stats, axis=1)}\t{np.max(stats, axis=0)}')

    # Minimum/Maximum value per-column in a multi-column array
    print(f'{np.min(stats, axis=0)}\t{np.max(stats, axis=1)}')

    # Sum of all items in matrix
    print(np.sum(stats))

    # sum of all items in a row / column
    print(f'{np.sum(stats, axis=1)}\t{np.sum(stats, axis=0)}')

### Reorganizing arrays

def reorganize():
    # Array in (2, 4) shape
    before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

    # Reshaping into 3-D (2, 2, 2) array --> can reshape into any array as long as number of values match (2, 4) / (4, 2) / (1, 8)...
    after = before.reshape((2, 2, 2))
    print(after)

    # Vertically stacking vectors
    vec1 = np.array([1, 2, 3, 4])
    vec2 = np.array([5, 6, 7, 8])

    print(np.vstack([(vec1, vec2) * 4]))

    # Horizontally stacking
    hor1 = np.zeros((3, 3))
    hor2 = np.ones((3, 2))

    print(np.hstack((hor1, hor2)))

### Load data from file, boolean masking and advanced indexing

def load_data():
    # Set file path variable
    fpath = r"C:\Users\yotam\Documents\Python\material\numpy_intro_number_list.txt"

    # Load data from path --> np.genfromtxt(pathlike=path, delimiter=what_separates_numbers, dtype=type_of_data_to_load_numbers_in)
    filedata = np.genfromtxt(fname=fpath, delimiter='\t', dtype='int16')

    # Index by query
    print(filedata[filedata > 50])

    # Index with a list
    print(filedata[[0, 1, 2, 3, 4]])

### Problem #2
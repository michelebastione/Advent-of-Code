import numpy as np
from copy import deepcopy
from itertools import product

with open('input24.txt') as file:
    raw_data = file.read().splitlines()

data = [[*line] for line in raw_data]
arr = np.zeros((7, 7), dtype=int)
arr[0, :] = arr[-1, :] = 2
arr[:, 0] = arr[:, -1] = 2
arr[1:-1, 1:-1] = (np.array(data) == '#')

def adjacent(array, x, y):
    return array[[x-1, x, x, x+1], [y, y-1, y+1, y]]

def transform(array):
    array_copy = deepcopy(array)
    for i, j in product(range(1, len(array)-1), repeat=2):
        if array[i, j]:
            if np.count_nonzero(adjacent(array, i, j) == 1) != 1:
                array_copy[i, j] = 0
        else:
            if 1 <= np.count_nonzero(adjacent(array, i, j) == 1) <= 2:
                array_copy[i, j] = 1
    return array_copy

def biodiversity(array):
    powers = np.array([[2**(i*len(array[0])+j)
                        for j in range(len(array[0]))]
                       for i in range(len(array))])
    return np.sum(powers * array)

#soluzione 1
all_transformations = set()
while True:
    bytes = arr.tobytes()
    if bytes in all_transformations:
        print(biodiversity(arr[1:-1, 1:-1]))
        break
    all_transformations.add(bytes)
    arr = transform(arr)

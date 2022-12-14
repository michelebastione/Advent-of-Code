import numpy as np
from itertools import product

with open('input8.txt') as file:
    temp = np.array([[*line] for line in file.read().splitlines()])
    trees = -1 * np.ones((101, 101), dtype=int)
    trees[1:100, 1:100] = temp


def istaller(array, x, y):
    top = array[:x, y]
    bottom = array[x+1:, y]
    left = array[x, :y]
    right = array[x, y+1:]

    return any(array[x, y] > direction.max() for direction in [top, bottom, left, right])


def score(array, x, y):
    top = array[:x, y][::-1]
    bottom = array[x+1:, y]
    left = array[x, :y][::-1]
    right = array[x, y+1:]

    total = 1
    for direction in top, bottom, left, right:
        count = 0
        for tree in direction:
            count += 1
            if tree >= array[x, y]:
                break
        total *= count

    return total


# solution 1
print(sum(istaller(trees, *coords) for coords in product(range(1, 100), repeat=2)))

# solution 2
print(max(score(trees[1:-1, 1:-1], *coords) for coords in product(range(99), repeat=2)))

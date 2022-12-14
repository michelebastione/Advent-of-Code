import numpy as np
from copy import deepcopy

with open('input11.txt') as file:
    raw_data = file.read().splitlines()
    grid = np.array([[*line] for line in raw_data])

class Automa:
    def __init__(self, cells):
        x, y = cells.shape
        self.array = np.full((x+2, y+2), '.')
        self.array[1: -1, 1: -1] = deepcopy(cells)

    def strictly_adjacent(self, x, y):
        return self.array[x-1: x+2, y-1: y+2]

    def widely_adjacent(self, x, y):
        hl = np.flip(self.array[x, :y])
        hr = self.array[x, y+1:]
        vu = np.flip(self.array[:x, y])
        vd = self.array[x+1:, y]
        adl = np.flip(self.array.diagonal(y-x)[:x]) if x < y else np.flip(self.array.diagonal(y-x)[:y])
        dl = self.array.diagonal(y-x)[x+1:] if x < y else self.array.diagonal(y-x)[y+1:]
        flipped = np.fliplr(self.array)
        y1 = self.array.shape[1]-1-y
        adr = np.flip(flipped.diagonal(y1-x)[:x]) if x < y1 else np.flip(flipped.diagonal(y1-x)[:y1])
        dr = flipped.diagonal(y1-x)[x+1:] if x < y1 else flipped.diagonal(y1-x)[y1+1:]
        counts = {'L': 0, '#': 0}
        for i in (hl, hr, vu, vd, adl, dl, adr, dr):
            for j in i:
                if j == 'L':
                    counts['L'] += 1
                    break
                if j == '#':
                    counts['#'] += 1
                    break
        return counts

    def solve_1(self):
        x, y = self.array.shape
        new_array = np.full((x, y), '.')
        while True:
            for i in range(1, x):
                for j in range(1, y):
                    if self.array[i, j] == 'L' and np.count_nonzero(self.strictly_adjacent(i, j) == '#') == 0:
                        new_array[i, j] = '#'
                    if self.array[i, j] == '#' and np.count_nonzero(self.strictly_adjacent(i, j) == '#') > 4:
                            new_array[i, j] = 'L'
            if (new_array == self.array).all():
                return np.count_nonzero(self.array == '#')
            self.array = deepcopy(new_array)

    def solve_2(self):
        x, y = self.array.shape
        new_array = np.full((x, y), '.')
        while True:
            for i in range(1, x):
                for j in range(1, y):
                    if self.array[i, j] == 'L' and self.widely_adjacent(i, j)['#'] == 0:
                        new_array[i, j] = '#'
                    if self.array[i, j] == '#' and self.widely_adjacent(i, j)['#'] >= 5:
                            new_array[i, j] = 'L'
            if (new_array == self.array).all():
                return np.count_nonzero(self.array == '#')
            self.array = deepcopy(new_array)

#soluzione 1
print(Automa(grid).solve_1())

#soluzione 2
print(Automa(grid).solve_2())


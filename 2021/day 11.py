import numpy as np
from itertools import product

with open('input11.txt') as file:
    octopi = np.array([[i for i in line.strip()] for line in file], dtype=int)


class Grid:
    def __init__(self, energy):
        self.energy_level = energy
        self.flashes = 0

    def adjacent(self, i, j):
        adj = []
        if i > 0:
            adj.append((i-1, j))
            if j > 0:
                adj.append((i-1, j-1))
            if j < 9:
                adj.append((i-1, j+1))
        if i < 9:
            adj.append((i+1, j))
            if j > 0:
                adj.append((i+1, j-1))
            if j < 9:
                adj.append((i+1, j+1))
        if j > 0:
            adj.append((i, j-1))
        if j < 9:
            adj.append((i, j+1))
        return adj

    def step(self):
        already_lit = []
        self.energy_level += 1
        while (self.energy_level >= 10).any():
            for p in product(range(10), repeat=2):
                if self.energy_level[p] >= 10 and p not in already_lit:
                    self.flashes += 1
                    already_lit.append(p)
                    self.energy_level[p] = 0
                    for q in self.adjacent(*p):
                        if self.energy_level[q] < 10 and q not in already_lit:
                            self.energy_level[q] += 1


grid_octo = Grid(octopi)

# soluzione 1
for _ in range(100):grid_octo.step()
print(grid_octo.flashes)

# soluzione 2
count = 100
while grid_octo.energy_level.any():
    grid_octo.step()
    count += 1
print(count)
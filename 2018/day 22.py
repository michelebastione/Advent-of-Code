import numpy as np
from itertools import product

depth = 6969
tx, ty = 9, 796

geological_index = np.zeros((ty + 1, tx + 1), dtype=int)
geological_index[0] = np.arange(tx + 1) * 16807
geological_index[:, 0] = np.arange(ty + 1) * 48271
erosion_level = (geological_index + depth) % 20183

for r, c in product(range(1, ty + 1), range(1, tx + 1)):
    if (r, c) == (ty, tx):
        geological_index[r, c] = 0
    else:
        geological_index[r, c] = erosion_level[r - 1, c] * erosion_level[r, c - 1]
        erosion_level[r, c] = (geological_index[r, c] + depth) % 20183

#soluzione 1
terrain = erosion_level % 3
print(terrain.sum())

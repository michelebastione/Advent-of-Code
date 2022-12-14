import numpy as np
from itertools import product
with open('input9.txt') as file:
    hmap = np.array([[i for i in row.strip('\n')] for row in file], dtype=int)
    size_x, size_y = hmap.shape

def find_adjacent(i, j):
    adj = []
    if i > 0:
        adj.append((i-1, j))
    if i < size_x-1:
        adj.append((i+1, j))
    if j > 0:
        adj.append((i, j-1))
    if j < size_y-1:
        adj.append((i, j+1))
    return adj


# soluzione 1
risk_level = 0
lowest_points = []
for x, y in product(range(size_x), range(size_y)):
    num = hmap[x, y]
    if num < min(hmap[i, j] for i, j in find_adjacent(x, y)):
        lowest_points.append((x, y))
        risk_level += num + 1
print(risk_level)

# soluzione 2
def find_basin(i, j):
    if (i, j) not in lowest_points:
        flow = min(find_adjacent(i, j), key=lambda x: hmap[x])
        return find_basin(*flow)
    else:
        return i, j

all_points = [*product(range(size_x), range(size_y))]
basins = {}
for i in range(size_x):
    for j in range(size_y):
        if hmap[i, j] != 9:
            basins[i, j] = find_basin(i, j)

all_basins = {b: [p for p in basins if basins[p] == b] for b in lowest_points}
a, b, c, *d = sorted([len(value) for value in all_basins.values()], reverse=True)
print(a*b*c)
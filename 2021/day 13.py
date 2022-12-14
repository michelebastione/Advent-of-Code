import numpy as np
import re

grid = np.zeros((500, 500), dtype=int)
with open('input13.txt') as file:
    coords, folds = file.read().split('\n\n')


for c in coords.splitlines():
    x, y = map(int, c.split(','))
    i, j = grid.shape
    if x >= j:
        grid = np.append(grid, np.zeros((i, x-j+1), dtype=int), 1)
    if y >= i:
        grid = np.append(grid,np.zeros((y-i+1, j), dtype=int), 0)
    grid[y, x] = 1

def fold(paper, axis, coord):
    i, j = paper.shape
    if axis == 'x':
        flipped = np.fliplr(paper[:, coord+1:])
        new_paper = np.delete(paper, np.s_[coord:], 1)
        new_paper[:, coord-j+1:] |= flipped
    else:
        flipped = np.flipud(paper[coord+1:, :])
        new_paper = np.delete(paper, np.s_[coord:], 0)
        new_paper[coord-i+1:, :] |= flipped
    return new_paper

# soluzione 1
print(np.count_nonzero(fold(grid, 'x', 655)))

# soluzione 2
for f in folds.splitlines():
    match = re.search(r'([xy])=(\d+)', f)
    axis, line = match.group(1), int(match.group(2))
    grid = fold(grid, axis, line)
print(*[' '.join(['#' if r else ' ' for r in row]) for row in grid], sep='\n')

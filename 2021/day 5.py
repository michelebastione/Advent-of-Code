import re
import numpy as np

with open('input5.txt') as file:
    raw_segments = file.read().splitlines()

segments = [[*map(int, re.findall(r'\d+', line))] for line in raw_segments]
horizontal_and_vertical = [*filter(lambda x: x[0]==x[2] or x[1]==x[3], segments)]
grid = np.zeros((1000, 1000), dtype=int)

# soluzione 1
for seg in horizontal_and_vertical:
    i, j = sorted(seg[::2])
    k, l = sorted(seg[1::2])
    grid[k: l+1, i: j+1] += 1
print(np.count_nonzero(grid > 1))

# soluzione 2
for seg in segments:
    if seg not in horizontal_and_vertical:
        i, j = seg[::2]
        k, l = seg[1::2]
        for _ in range(abs(j-i)+1):
            grid[k, i] += 1
            i = i+1 if i<j else i-1
            k = k+1 if k<l else k-1
print(np.count_nonzero(grid > 1))

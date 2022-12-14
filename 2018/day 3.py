import numpy as np
import re

with open('input3.txt') as file:
    data = []
    for line in file.read().splitlines():
        data.append(dict())
        data[-1]['id'] = int(re.search(r'#(\d+)', line).group(1))
        data[-1]['pos'] = [int(i) for i in re.search(r'(?<=@ )\d+,\d+', line).group(0).split(',')]
        data[-1]['dim'] = [int(i) for i in re.search(r'(?<=: )\d+y\d+', line).group(0).split('y')]

fabric = np.zeros((1000, 1000))
for line in data:
    p = line['pos']
    d = line['dim']
    rect = fabric[p[1]:p[1]+d[1], p[0]:p[0]+d[0]]
    rect[rect == 1] = 2
    rect[rect == 0] = 1

#soluzione 1 (un po' convoluta ma efficientissima)
print(np.count_nonzero(fabric == 2))

#soluzione 2 (anche questa molto efficiente)
for line in data:
    p = line['pos']
    d = line['dim']
    rect = fabric[p[1]:p[1]+d[1], p[0]:p[0]+d[0]]
    if np.all(rect == 1):
        print(line['id'])
        break
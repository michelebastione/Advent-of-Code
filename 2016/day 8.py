import numpy as np
import re
from collections import deque

with open('input8.txt') as file:
    data = file.read().splitlines()

display = np.array([['.']*50]*6)

for line in data:
    if 'rect' in line:
        rect = line.split()[1]
        l, h = rect.split('y')
        display[:int(h), :int(l)] = '#'
    else:
        n, shift = [int(k) for k in re.findall(r'\d+', line)]
        if 'row' in line:
            temp = deque(display[n, :])
            temp.rotate(shift)
            display[n, :] = temp
        else:
            temp = deque(display[:, n])
            temp.rotate(shift)
            display[:, n] = temp

#soluzione 1
print(np.count_nonzero(display=='#'))

#soluzione 2 (è un po' difficile da visualizzare)
for i in range(10):
    print(display[:, i*5 : i*5+4])
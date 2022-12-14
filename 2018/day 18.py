import numpy as np
from copy import deepcopy
from itertools import product

with open('input18.txt') as file:
    data = file.read().splitlines()

acres = np.array([['E']*52]*52)
for i in range(0, 50):
    acres[i+1, 1: 51] = list(data[i])

def lumber_collection(field):
    updated_field = deepcopy(field)
    l = len(field) - 1
    for i, j in product(range(1, l), repeat=2):
        adjacent = field[i-1: i+2, j-1: j+2]
        if field[i, j] == '.':
            updated_field[i, j] = '|' if np.count_nonzero(adjacent == '|') >= 3 else '.'
        elif field[i, j] == '|':
            updated_field[i, j] = '#' if np.count_nonzero(adjacent == '#') >= 3 else '|'
        else:
            if np.count_nonzero(adjacent == '#') >= 2 and np.count_nonzero(adjacent == '|') >= 1:
                updated_field[i, j] = '#'
            else:
                updated_field[i, j] = '.'
    return updated_field

#soluzione 1
new_field = acres
for i in range(10):
    new_field = lumber_collection(new_field)
print(np.count_nonzero(new_field == '#') * np.count_nonzero(new_field == '|'))

count = 0
first_cycle = []
next_field = acres
while True:
    next_field = lumber_collection(next_field)
    nfb = next_field.tobytes()
    if nfb in first_cycle:
        break
    first_cycle.append(nfb)
    count += 1

#soluzione 2 (abbastanza efficiente anche se leggermente convoluta)
acyclic = first_cycle.index(nfb)
len_cycle = count - acyclic
steps_left = (10**9 - acyclic) % len_cycle

final_field = acres
for i in range(acyclic + steps_left):
    final_field = lumber_collection(final_field)
print(np.count_nonzero(final_field == '#') * np.count_nonzero(final_field == '|'))
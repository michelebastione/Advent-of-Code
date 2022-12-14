import numpy as np
from copy import deepcopy

with open('input3.txt') as file:
    rows = file.read().splitlines()
    consumption = np.array([[*line] for line in rows], dtype=int)
    trans = consumption.transpose()

#soluzione 1
gamma = [str(np.argmax(np.bincount(col))) for col in trans]
eps = [str(np.argmin(np.bincount(col))) for col in trans]
g = int(''.join(gamma), 2)
e = int(''.join(eps), 2)
print(g*e)

#soluzione 2
def rating(array, r):
    a = deepcopy(array)
    func = np.argmax if r == 'o2' else np.argmin
    value = 1 if r == 'o2' else 0

    index = 0
    while len(a) > 1:
        c = np.bincount(a[:, index])
        c0, c1 = c
        if c0 == c1:
            a = a[np.where(a[:, index] == value)]
        else:
            a = a[np.where(a[:, index] == func(c))]
        index += 1

    return a[0]

def decode(b):
    return int(''.join([*map(str, b)]), 2)

o2 = rating(consumption, 'o2')
co2 = rating(consumption, 'co2')

print(decode(o2)*decode(co2))

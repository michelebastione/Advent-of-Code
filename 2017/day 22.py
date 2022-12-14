import numpy as np
from itertools import count

with open('input22.txt') as file:
    data_raw = file.read().splitlines()
    data = np.array([[i for i in j] for j in data_raw]) == '#'

def turn(instr, orientation):
    new_direction = 1 if instr else -1
    to_exec = {
        i:
            f"current[{not i % 2}] {'-' if i//2 else '+'}= {new_direction}"
        for i in range(4)
    }
    exec(to_exec[orientation])
    return (orientation + new_direction) % 4

def dont_turn(instr, orientation):
    to_exec = {
        i:
            f"current[{i % 2}] {'-' if i in (0, 3) else '+'}= {1 if instr == 2 else -1}"
        for i in range(4)
    }
    exec(to_exec[orientation])
    return orientation if instr == 2 else (orientation + 2) % 4

#soluzione 1
grid = np.zeros((10000, 10000), dtype=bool)
grid[4988: 5013, 4988: 5013] = data
current = [5000, 5000]
dir = infections = 0

for i in range(10000):
    x, y = current
    dir = turn(grid[x, y], dir)
    if not grid[x, y]:
        infections += 1
    grid[x, y] = not grid[x, y]

print(infections)

#soluzione 2 (le funzioni usate sono altamente inefficienti in quanto costruiscono un dizionario per ogni iterazione. Da ottimizzare se possibile)
grid = np.zeros((10000, 10000), dtype=int)
grid[4988: 5013, 4988: 5013] = data
current = [5000, 5000]
dir = infections = 0

for i in range(10**7):
    x, y = current
    value = grid[x, y]
    if value in (0, 1):
        dir = turn(value, dir)
        grid[x, y] += 2
    else:
        dir = dont_turn(value, dir)
        if value == 2:
            infections += 1
            grid[x, y] = 1
        else:
            grid[x, y] = 0

print(infections)

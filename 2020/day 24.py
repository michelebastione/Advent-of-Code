import re
from copy import deepcopy
from itertools import product

with open('input24.txt') as file:
    raw_data = file.read().splitlines()
data = [re.findall(r'[ns]?[ew]', line) for line in raw_data]

def move(route, start=(0, 0)):
    x, y = start
    for i in route:
        if i == 'e':
            x += 1
        if i == 'w':
            x -= 1
        if i == 'nw':
            y -= 1
            x -= 1 if y % 2 == 0 else 0
        if i == 'sw':
            y += 1
            x -= 1 if y % 2 == 0 else 0
        if i == 'ne':
            y -= 1
            x += 0 if y % 2 == 0 else 1
        if i == 'se':
            y += 1
            x += 0 if y % 2 == 0 else 1
    return x, y

black_tiles = set()
for i in data:
    coords = move(i)
    if coords in black_tiles:
        black_tiles.remove(coords)
    else:
        black_tiles.add(coords)

#soluzione 1
print(len(black_tiles))

def adjacent(tile):
    adj = set()
    for dir in ('e', 'se', 'sw', 'w', 'ne', 'nw'):
        adj.add(move([dir], tile))
    return adj

copy_tiles = deepcopy(black_tiles)
def flip(tile):
    adj_tiles = adjacent(tile)
    if len(adj_tiles & black_tiles) not in (1, 2):
        copy_tiles.remove(tile)
    for a in adj_tiles:
        if a not in black_tiles:
            if len(black_tiles & adjacent(a)) == 2:
                copy_tiles.add(a)

for _ in range(100):
    for tile in black_tiles:
        flip(tile)
    black_tiles = deepcopy(copy_tiles)

#soluzione 2 (Sono contento dell'idea che ho avuto per risolvere questo problema, è piuttosto efficiente)
print(len(black_tiles))
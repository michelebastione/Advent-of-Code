from itertools import product
from numpy import Inf

favorite_number = 1362
rule_of_walls = lambda x, y: bin((x+y)**2 + 3*x + y + favorite_number).count('1') % 2
adjacent = lambda x, y: {(x+1, y), (x-1, y), (x, y+1), (x, y-1)}.intersection(grid)

grid = set()
for p in product(range(50), range(50)):
    if not rule_of_walls(p[0], p[1]):
        grid.add(p)

def dijkstra():
    unvisited = [*grid]
    tentative = {node: Inf for node in unvisited}
    tentative[(1, 1)] = 0
    current = (1, 1)
    while unvisited:
        for i in adjacent(*current):
            if i in unvisited:
                tentative[i] = min(tentative[i], tentative[current]+1)
        unvisited.remove(current)
        if unvisited:
            current = min(unvisited, key=lambda x: tentative[x])
    return tentative

#soluzioni 1 & 2 (non riciclabili per il momento)
distances = dijkstra()
print(distances[(31, 39)], sum(1 for i in distances.values() if i <= 50))

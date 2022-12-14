import numpy as np
from itertools import product

with open('input15.txt') as file:
    graph = np.array([[*row[:-1]] for row in file], dtype=int)


def prod(x, y):
    return product(range(x), range(y))


def find_adjacent(i, j):
    adj = []
    if i > 0:
        adj.append((i-1, j))
    if i < 99:
        adj.append((i+1, j))
    if j > 0:
        adj.append((i, j-1))
    if j < 99:
        adj.append((i, j+1))
    return adj

# soluzione 1
def dijkstra(array):
    x, y = array.shape
    distance = {p: np.inf for p in prod(x, y)}
    unmarked = {*prod(x, y)}
    distance[(0, 0)] = 0
    while (x-1, y-1) in unmarked:
        current = min(unmarked, key=lambda n: distance[n])
        if current[0]%10 == current[1]%10 == 0:
            print(current)
        for v in find_adjacent(*current):
            distance[v] = min(distance[v], distance[current] + array[v])
        unmarked.remove(current)
    return distance[x-1, y-1]

print(dijkstra(graph))

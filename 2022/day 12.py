from string import ascii_lowercase as abc
from math import inf

elevation = {}
indexing = {char: n for n, char in enumerate(abc)}
with open('input12.txt') as file:
    for m, line in enumerate(file):
        for n, char in enumerate(line.strip()):
            if char == "S":
                current_position = (m, n)
                elevation[current_position] = 0
            elif char == "E":
                best_position = (m, n)
                elevation[best_position] = 25
            else:
                elevation[(m, n)] = indexing[char]


def can_reach(grid, pos):
    x, y = pos
    adjacents = []
    for adj in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if adj in grid and grid[pos] <= grid[adj]+1:
            adjacents.append(adj)
    return adjacents


def dijkstra(grid, start):
    unvisited = [*grid]
    tentative = {node: inf for node in unvisited}
    tentative[start] = 0
    current = start
    while unvisited:
        for i in can_reach(grid, current):
            if i in unvisited:
                tentative[i] = min(tentative[i], tentative[current]+1)
        unvisited.remove(current)
        if unvisited:
            current = min(unvisited, key=lambda x: tentative[x])
    return tentative


distances = dijkstra(elevation, best_position)

# solution 1
print(distances[current_position])

# solution 2
all_starting_points = filter(lambda x: not elevation[x], distances)
shortest_hike = min(all_starting_points, key=lambda x: distances[x])
print(distances[shortest_hike])

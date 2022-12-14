import numpy as np
from itertools import permutations

with open('input9.txt') as file:
    data = file.read().splitlines()

raw_distances = [[i.split(' to ') for i in line.split(' = ')] for line in data]
cities = set(i[0][0] for i in raw_distances)
cities.add(raw_distances[-1][0][1])

cities_to_index = dict(zip(cities, range(len(cities))))

adjacency_matrix = np.zeros((8, 8), dtype=int)
for distance in raw_distances:
    adjacency_matrix[cities_to_index[distance[0][0]], cities_to_index[distance[0][1]]] = distance[1][0]
    adjacency_matrix[cities_to_index[distance[0][1]], cities_to_index[distance[0][0]]] = distance[1][0]

minimo = np.Inf
massimo = 0
for permutation in permutations(range(8)):
    permutation1 = [*permutation][:-1]
    permutation2 = [*permutation][1:]
    temp = sum(adjacency_matrix[perm[0], perm[1]] for perm in zip(permutation1, permutation2))
    minimo = min(minimo, temp)
    massimo = max(massimo, temp)

#soluzioni 1 & 2
print(minimo, massimo)
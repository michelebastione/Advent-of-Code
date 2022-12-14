import numpy as np
from itertools import permutations

with open('input13.txt') as file:
    data = file.read().splitlines()

raw_happyness = [line.split() for line in data]
people = set(person[0] for person in raw_happyness)

people_to_index = dict(zip(people, range(len(people))))

adjacency_matrix = np.zeros((9, 9), dtype=int)

for person in raw_happyness:
    value = int(person[3]) * [1, -1]['lose' in person]
    adjacency_matrix[people_to_index[person[0]], people_to_index[person[-1].rstrip('.')]] = value

def optimal_value(matrix):
    massimo = 0
    for permutation in permutations(range(len(matrix))):
        perm1 = [*permutation]
        perm2 = [*[*permutation][1:], permutation[0]]
        temp = sum(matrix[perm[0], perm[1]] + matrix[perm[1], perm[0]] for perm in zip(perm1, perm2))
        massimo = max(massimo, temp)
    return massimo

#soluzione 1
print(optimal_value(adjacency_matrix[:8, :8]))

#soluzione 2
print(optimal_value(adjacency_matrix))
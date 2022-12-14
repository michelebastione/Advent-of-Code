import re
from itertools import permutations
import numpy as np

with open('input22.txt') as file:
    data = file.read().splitlines()[2:]

nodes = dict()
for line in data:
    stats = [*map(int, re.findall(r'\d+', line))]
    nodes[(stats[0], stats[1])] = stats[3: 5]

#soluzione 1
viable_pairs = 0
removable_nodes = set()
for node_a, node_b in permutations(nodes, 2):
    a, b = nodes.get(node_a), nodes.get(node_b)
    if 0 < a[0] <= b[1]:
        removable_nodes.add(node_a)
        viable_pairs += 1
print(viable_pairs)

empty_node = (4, 25)    #controllato manualmente
non_removable_nodes = set(nodes) - removable_nodes - {empty_node}
a = np.zeros((30, 34))
for i in non_removable_nodes:
    a[i[1], i[0]] = 1

#   L'ARRAY CI MOSTRA UN MURO CHE VA DA (2, 2) A (33, 2)
#   PER AGGIRARLO E ARRIVARE A (33, 0) DA (4, 25) CI VOGLIONO 60 MOSSE
#   A QUESTO PUNTO I DATI SI TROVERANNO NELLA CASELLA (32, 0)
#   IL CICLO NECESSARIO PER SPOSTARLI DI CASELLA IN CASELLA COSTA 5 MOSSE
#   NE SUSSEGUE CHE PER ARRIVARE A (0, 0) NECESSITEREMO DI:

#soluzione 2
print(60 + 5*32)

from itertools import combinations
from copy import deepcopy

with open('input25.txt') as file:
    data = file.read().splitlines()
points = [list(map(int, line.split(','))) for line in data]

def manhattan(p1, p2):
    return sum(abs(i - j) for i, j in zip(p1, p2))

constellations = {0: [points[0]]}
current = 0
for point in points[1:]:
    check = False
    for i in range(current + 1):
        if any(manhattan(point, j) <= 3 for j in constellations[i]):
            constellations[i].append(point)
            check = True
            break
    if not check:
        current += 1
        constellations[current] = [point]

#soluzione 1 (impiega 3 minuti graph terminare, ma non so se ho voglia di ottimizzarla)
joined_constellations = dict()
while constellations != joined_constellations:
    joined_constellations = deepcopy(constellations)
    for combs in combinations(constellations, 2):
        check = False
        const1, const2 = combs
        for c1 in constellations[const1]:
            if any(manhattan(c1, c2) <= 3 for c2 in constellations[const2]):
                check = True
                constellations[const1].extend(constellations[const2])
                del constellations[const2]
                break
        if check:
            break
    if len(constellations) %10 == 0:
        print(len(constellations))

print(len(constellations))
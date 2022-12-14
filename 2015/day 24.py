from itertools import combinations
from math import inf

with open('input24.txt') as file:
    gifts = [int(i) for i in file.read().splitlines()]

s = sum(gifts)

def prod(iterable):
    p = 1
    for i in iterable:
        p *= i
    return p

qe = inf
group = 2
while qe == inf:
    for combination in filter(lambda x: sum(x) == 520, combinations(gifts, group)):
        for i in range(5, 18):
            if any(sum(comb) == 520 for comb in combinations(filter(lambda x: x not in combination, gifts), i)):
                qe = min(qe, prod(combination))
    group += 1

#soluzione 1
print(qe)

from itertools import permutations
from math import ceil

with open('input15.txt') as file:
    data = file.read().splitlines()

ingredients = []
for line in data:
    ingredient, quantities = line.split(': ')
    ingredients.append([int(prop.split()[1]) for prop in quantities.split(', ')])


def partitioned_sequences(n, k):
    if k == 2:
        for i in range(1, n//2+1):
            yield (i, n-i)
    else:
        results = set()
        for i in range(ceil(n/k), n-k+2):
            subp = partitioned_sequences(n-i, k-1)
            for j in subp:
                temp = (*j, i)
                if hash(temp) in results:
                    continue
                results.update(hash(perm) for perm in permutations(temp))
                yield temp

def prod(iterable):
    p = 1
    for it in iterable:
        p *= it
    return p

def highest_score(values, calories=False):
    maximum = 0
    if not calories:
        values = [value[:-1] for value in values]
    for sequence in partitioned_sequences(100, 4):
        for permutation in permutations(values):
            zipped = zip(sequence, permutation)
            multiplied = [*map(lambda x: [x[0]*y for y in x[1]], zipped)]
            properties = [sum(mult[i] for mult in multiplied) for i in range(5 if calories else 4)]
            if any(prop < 0 for prop in properties) or (calories and properties[-1] != 500):
                continue
            maximum = max(maximum, prod(properties[:4]))
    return maximum

#soluzione 1
print(highest_score(ingredients))

#soluzione 2
print(highest_score(ingredients, True))
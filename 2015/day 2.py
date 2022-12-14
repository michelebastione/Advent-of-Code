from itertools import combinations

with open ('input2.txt') as file:
    gifts = [[int(factor) for factor in line.split('x')]
            for line in file.read().splitlines()]

def prod(iter):
    result = 1
    for i in iter:
        result *= i
    return result

total_wrap = 0
for gift in gifts:
    areas = [prod(combination) for combination in combinations(gift, 2)]
    total_wrap += 2*sum(areas)+min(areas)
print(total_wrap)

total_ribbon = 0
for gift in gifts:
    perimeters = [sum(combination) for combination in combinations(gift, 2)]
    total_ribbon += 2*min(perimeters)+prod(gift)
print(total_ribbon)

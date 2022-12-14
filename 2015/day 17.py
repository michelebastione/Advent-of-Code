from itertools import combinations

with open('input17.txt') as file:
    containers = sorted([int(container) for container in file.read().splitlines()])

count = 0
for i in range(4, 11):
    count += sum(1 for combination in combinations(containers, i) if sum(combination) == 150)

#soluzione 1
print(count)

count_min = 0
n = 4
while count_min == 0:
    count_min += sum(1 for combination in combinations(containers, n) if sum(combination) == 150)
    n += 1

#soluzione 2
print(count_min)
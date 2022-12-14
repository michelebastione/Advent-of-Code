from itertools import product

with open('input6.txt') as file:
    data = file.read().splitlines()

# data = """1, 1
# 1, 6
# 8, 3
# 3, 4
# 5, 5
# 8, 9""".splitlines()


points = {i: [int(j) for j in data[i].split(',')] for i in range(len(data))}
distances_basic = {d: 0 for d in points}
distances_increased = {d: 0 for d in points}
less_than_10k = 0

man_distance = lambda x, y: abs(x[0]-y[0]) + abs(x[1]-y[1])
sum_distances = lambda x: sum(man_distance(x, p) for p in points.values())

for p in product(range(-50, 351), repeat=2):
    distances = {i: man_distance(p, points[i]) for i in points}
    temp = min(distances.items(), key=lambda x: x[1])

    if [*distances.values()].count(temp[1]) == 1:
        if -50 < p[0] < 350 and -50 < p[1] < 350:
            distances_basic[temp[0]] += 1
        distances_increased[temp[0]] += 1

    if sum_distances(p) < 10000:
        less_than_10k += 1

#soluzione 1 (un po' rozza, si può ottimizzare di molto eliminando i quattro "angoli" che estendono la griglia all'infinito)
finite_distances = {i: distances_basic[i] for i in distances_basic if distances_basic[i] == distances_increased[i]}
print(max(finite_distances.items(), key=lambda x: x[1])[1])

#soluzione 2
print(less_than_10k)
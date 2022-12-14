import numpy as np
from fractions import Fraction

with open('input10.txt') as file:
    raw_data = file.read().splitlines()[::-1]
raw_data=""".#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##""".splitlines()[::-1]
data = np.array([[char for char in row] for row in raw_data])
coord = [*zip(*np.nonzero(data == '#'))]

def calculate_coefficient(p1, p2):
    x1, y1 = map(int, p1)
    x2, y2 = map(int, p2)
    if y1 - y2 == 0:
        return np.inf
    elif x1 - x2 == 0:
        return 0
    else:
        return Fraction(x1-x2, y1-y2)

def all_coefficients(p1):
    coefficients = dict()
    for p2 in coord:
        if p1 == p2:
            continue
        coeff = calculate_coefficient(p1, p2)
        relative_position = p2[0] > p1[0] if coeff == np.inf else p2[1] > p1[1]
        if coeff in coefficients:
            coefficients[coeff].add(relative_position)
        else:
            coefficients[coeff] = {relative_position}
    return coefficients

def closest_point(origin, points, coeff, dir):
    x1, y1 = origin
    alligned = []
    for point in points:
        x2, y2 = point
        if coeff == np.inf:
            if (dir and x2 > x1) or (not dir and x2 < x1):
                alligned.append(point)
        else:
            if (dir and y2 > y1) or (not dir and y2 < y1):
                alligned.append(point)
    if len(alligned) == 0:
        return None
    return min(alligned, key=lambda p: (x1-p[0])**2 + (y1-p[1])**2)

intersections = dict()
for c1 in coord:
    all_c1_coeffs = all_coefficients(c1)
    intersections[c1] = sum(len(i) for i in all_c1_coeffs.values())

#soluzione 1
optimal_station, asteroids = max(intersections.items(), key=lambda x: x[1])
print(asteroids)

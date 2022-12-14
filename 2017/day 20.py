import re
from sympy import Symbol
from sympy.solvers import solve
from itertools import combinations, product

with open('input20.txt') as file:
    data = file.read().splitlines()

position_function = lambda p, v, a, t: p + v*t + a*t**2/2
arguments = []
min_pos = 10**100

for i in range(len(data)):
    args = [[*map(int, re.findall(r'-?\d+', arg))] for arg in data[i].split()]
    arguments.append(args)
    manhattan = 0
    p, v ,a = args
    for j in range(3):
        manhattan += abs(position_function(p[j], v[j], a[j], 10**10))
    if manhattan < min_pos:
        min_pos = manhattan
        min_particle = i

#soluzione 1
print(min_particle)

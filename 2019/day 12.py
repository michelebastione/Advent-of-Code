import re
from itertools import combinations

with open('input12.txt') as file:
    data = file.read().splitlines()

class Moon():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vx = self.vy = self.vz = 0

    def potential(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def kinetic(self):
        return abs(self.vx) + abs(self.vy) + abs(self.vz)

moons = [Moon(*map(int, re.findall(r'-?\d+', line))) for line in data]
# positions = [dict(zip('xyz', map(int, re.findall(r'-?\d+', line)))) for line in data]
# objects = [dict(zip(['pos', 'vel'], [pos, [0]*3])) for pos in positions]

def apply_gravity():
    for c1, c2 in combinations(moons, 2):
        if c1.x != c2.x:
            c1.vx += 1 if c1.x < c2.x else -1
            c2.vx += 1 if c1.x > c2.x else -1
        if c1.y != c2.y:
            c1.vy += 1 if c1.y < c2.y else -1
            c2.vy += 1 if c1.y > c2.y else -1
        if c1.z != c2.z:
            c1.vz += 1 if c1.z < c2.z else -1
            c2.vz += 1 if c1.z > c2.z else -1

def update_positions():
    for moon in moons:
        moon.x += moon.vx
        moon.y += moon.vy
        moon.z += moon.vz

for i in range(1000):
    apply_gravity()
    update_positions()

#soluzione 1
print(sum(moon.potential()*moon.kinetic() for moon in moons))
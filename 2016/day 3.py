import re
import numpy as np

with open('input3.txt') as file:
    data = file.read().splitlines()

count = 0
for line in data:
    sides = sorted([int(i) for i in re.findall(r'\d+', line)])
    count += 1 if sum(sides[:2]) > sides[2] else 0

#soluzione 1
print(count)

count = 0
for i in range(0, len(data), 3):
    temp = np.array([[int(k) for k in re.findall(r'\d+', line)] for line in data[i:i+3]])
    for column in np.rot90(temp):
        sides = sorted(column)
        count += 1 if sum(sides[:2]) > sides[2] else 0
print(count)
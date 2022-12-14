import re
from itertools import product

with open('input23.txt') as file:
    data_raw = file.read().splitlines()

ordered_data = [list(map(int, re.findall(r'-?\d+', line))) for line in data_raw]
data = {tuple(i[:3]): i[3] for i in ordered_data}

def manhattan(p1, p2):
    return sum(abs(i[0] - i[1]) for i in zip(p1, p2))

#soluzione 1
max_signal = max(data.items(), key=lambda x: x[1])
print(sum(1 for point in data if manhattan(max_signal[0], point) <= max_signal[1]))

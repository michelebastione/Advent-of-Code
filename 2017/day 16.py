import re
from collections import deque

with open('input16.txt') as file:
    data = file.read().split(',')

current_order = 'abcdefghijklmnop'

swap = lambda s, i1, i2: s[: i1]+s[i2]+s[i1+1: i2]+s[i1]+s[i2+1: ]

def rotate(s, i):
    temp = deque(s)
    temp.rotate(i)
    return ''.join(temp)

def dance(programs):
    for instr in data:
        if instr[0] == 'y':
            indices = sorted(map(int, re.findall(r'\d+', instr)))
            programs = swap(programs, *indices)
        if instr[0] == 'p':
            indices = sorted(map(programs.index, [instr[1], instr[3]]))
            programs = swap(programs, *indices)
        if instr[0] == 's':
            programs = rotate(programs, int(instr[1:]))
    return programs

#soluzione 1
current_order = dance(current_order)
print(current_order)

#soluzione 2 (va un po' graph sfruttare il caso fortuito dell'input ma è estremamente efficiente)
count = 1
while current_order != 'abcdefghijklmnop':
    current_order = dance(current_order)
    count += 1

for i in range(10**9 % 48):
    current_order = dance(current_order)
print(current_order)

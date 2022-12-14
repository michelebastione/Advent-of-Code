import re

with open('input23.txt') as file:
    data = file.read().splitlines()

registers = dict(zip('abcdefgh', [0]*8))

pointer = 0
count = 0

while 0 <= pointer < len(data):
    instr, reg, value = data[pointer].split()
    value = registers[value] if value.isalpha() else int(value)
    if instr == 'set':
        registers[reg] = value
    elif instr == 'sub':
        registers[reg] -= value
    elif instr == 'mul':
        registers[reg] *= value
        count += 1
    else:
        temp = registers[reg] if reg.isalpha() else int(reg)
        pointer += value-1 if temp != 0 else 0
    pointer += 1

#soluzione 1
print(count)


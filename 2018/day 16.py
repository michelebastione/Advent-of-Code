import re
from copy import deepcopy

all_opcodes = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori',
               'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']

with open('input16.txt') as file:
    raw_samples, raw_test = file.read().split("\n"*4)
    samples = []
    program = []
    for sample in raw_samples.split('\n\n'):
        lines = sample.splitlines()
        samples.append({line: [*map(int, re.findall(r'\d+', lines[line]))] for line in range(3)})
    for line in raw_test.splitlines():
        program.append([*map(int, re.findall(r'\d+', line))])

def compute(registers, instructions, opcode):
    a, b, c = instructions
    opcodes = {
        'addr': registers[a] + registers[b],
        'addi': registers[a] + b,
        'mulr': registers[a] * registers[b],
        'muli': registers[a] * b,
        'banr': registers[a] & registers[b],
        'bani': registers[a] & b,
        'borr': registers[a] | registers[b],
        'bori': registers[a] | b,
        'setr': registers[a],
        'seti': a,
        'gtir': 1 if a > registers[b] else 0,
        'gtri': 1 if registers[a] > b else 0,
        'gtrr': 1 if registers[a] > registers[b] else 0,
        'eqir': 1 if a == registers[b] else 0,
        'eqri': 1 if registers[a] == b else 0,
        'eqrr': 1 if registers[a] == registers[b] else 0
    }
    registers[c] = opcodes[opcode]
    return registers

def possible_matches(sample):
    count = 0
    possible = [sample[1][0], []]
    for opcode in all_opcodes:
        c_sample = deepcopy(sample)
        if sample[2] == compute(c_sample[0], c_sample[1][1:], opcode):
            count += 1
            possible[1].append(opcode)
    return count, possible

#soluzione 1
print(sum(1 for sample in samples if possible_matches(sample)[0] >= 3))

all_possibilities = [possible_matches(sample)[1] for sample in samples]
matches = dict(zip(range(16), [None]*16))

while not all(matches.values()):
    copy_possibilities = deepcopy(all_possibilities)
    for poss in all_possibilities:
        p1, p2 = poss
        if len(p2) == 1 and not matches[p1]:
            matches[p1] = p2[0]
            for p in copy_possibilities:
                if p2[0] in p[1]:
                    p[1].remove(p2[0])
            all_possibilities = copy_possibilities
            break

current_registers = [0, 0, 0, 0]
for instruction in program:
    current_registers = compute(current_registers, instruction[1:], matches[instruction[0]])

#soluzione 2
print(current_registers[0])
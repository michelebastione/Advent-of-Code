from copy import copy

with open('input7.txt') as file:
    data = file.read().splitlines()

instructions = {}
for instruction in data:
    instr = instruction.split(' -> ')
    instructions[tuple(instr[0].split())] = instr[1]

addresses = {'a': None}
for instruction in instructions:
    if len(instruction) == 1 and instruction[0].isdigit():
        addresses[instructions[instruction]] = int(instruction[0])
        continue
    for address in instruction:
        if address.islower() and address not in addresses:
            addresses[address] = None
new_addresses = copy(addresses)

def wires(memory):
    while memory['a'] is None:
        for instruction in instructions:
            instr = instructions[instruction]
            if any(memory[i] is None for i in instruction if i.islower()):
                continue
            elif 'NOT' in instruction:
                if instruction[1].isdigit():
                    memory[instr] = 2**16-int(instruction[1])-1
                else:
                    memory[instr] = 2**16-memory[instruction[1]]-1
            elif len(instruction) > 1:
                x = int(instruction[0]) if instruction[0].isdigit() else memory[instruction[0]]
                y = int(instruction[2]) if instruction[2].isdigit() else memory[instruction[2]]
                
                if 'AND' in instruction:
                    memory[instr] = x & y
                elif 'OR' in instruction:
                    memory[instr] = x | y
                elif 'LSHIFT' in instruction:
                    memory[instr] = x << y
                elif 'RSHIFT' in instruction:
                    memory[instr] = x >> y
                else:
                    pass

            elif instr == 'a':
                memory['a'] = memory[instruction[0]]

    return memory['a']

#soluzione 1
s1 = wires(addresses)
print(s1)

#soluzione 2
new_addresses['b'] = s1
print(wires(new_addresses))


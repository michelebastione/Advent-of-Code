with open('input19.txt') as file:
    instructions = file.read().splitlines()[1:]

def compute(registers, opcode, instructions):
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

def program(regs, register_pointer):
    pointer = 0
    while pointer < len(instructions):
        line = instructions[pointer].split()
        regs = compute(regs, line[0], map(int, line[1:]))
        regs[register_pointer] += 1
        pointer = regs[register_pointer]

    return regs

#soluzione 1 (impiega 30 secondi per terminare)
print(program([0]*30)[0])

with open('input23.txt') as file:
    instructions = file.read().splitlines()

def turing_lock(a, b):
    pointer = 0
    while pointer in range(len(instructions)):
        instruction = instructions[pointer]
        if 'inc' in instruction:
            if 'b' in instruction:
                b += 1
            else:
                a += 1
            pointer += 1
        elif 'hlf' in instruction:
            a //= 2
            pointer += 1
        elif 'tpl' in instruction:
            a *= 3
            pointer += 1
        elif 'jmp' in instruction:
            pointer += int(instruction.split()[1])
        elif 'jio' in instruction:
            if a == 1:
                pointer += int(instruction.split(', ')[1])
            else:
                pointer += 1
        elif 'jie' in instruction:
            if a%2 == 0:
                pointer += int(instruction.split(', ')[1])
            else:
                pointer += 1
    return b

#soluzione 1
print(turing_lock(0, 0))

#soluzione 2
print(turing_lock(1, 0))
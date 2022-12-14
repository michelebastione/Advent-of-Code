from copy import deepcopy

with open('input8.txt') as file:
    data = file.read().splitlines()
    

instructions = []
for line in data:
    instruction=line.split()
    instructions.append([instruction[0], int(instruction[1])])

def boot(program):
    accumulator = pointer = 0
    pointers = [0]
    while pointer<len(program):
        if program[pointer][0]=='acc':
         accumulator+=program[pointer][1]
         pointer+=1
        elif program[pointer][0]=='jmp':
         pointer+=program[pointer][1]
         if pointer in pointers:
          return False, accumulator
         pointers.append(pointer)
        else:
         pointer+=1
    return True, accumulator

#soluzione 1
print(boot(instructions))

for line in range(len(instructions)):
    original = instructions[line][0]
    instructions[line][0] = 'nop' if original == 'jmp' else 'jmp' if original == 'nop' else 'acc'
    result = boot(instructions)
    if result[0]:
        break
    instructions[line][0] = original

#soluzione 2
print(result)

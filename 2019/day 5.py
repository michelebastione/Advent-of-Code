import re

with open('input5.txt') as file:
    data = [*map(int, file.read().split(','))]

def execute(array, inp=1):
    instr = [*array]
    pointer = 0
    outputs = []
    while True:
        to_exec = instr[pointer]
        if to_exec == 99:
            break

        temp = str(to_exec)
        opcode =  to_exec if len(temp) < 2 else int(temp[-2:])
        parameter_1 = 0 if len(temp) < 3 else int(temp[-3])
        parameter_2 = 0 if len(temp) < 4 else int(temp[-4])
        parameter_3 = 0 if len(temp) < 5 else 1

        p1 = (instr[pointer+1], pointer+1)[parameter_1]
        if opcode == 3:
            instr[p1] = inp
            pointer += 2
        elif opcode == 4:
            outputs.append(instr[p1])
            pointer += 2
        else:
            p2 = (instr[pointer+2], pointer+2)[parameter_2]
            if opcode == 5:
                if instr[p1] != 0:
                    pointer = instr[p2]
                else:
                    pointer += 3
            elif opcode == 6:
                if instr[p1] == 0:
                    pointer = instr[p2]
                else:
                    pointer += 3
            else:
                p3 = (instr[pointer+3], pointer+3)[parameter_3]
                if opcode == 1:
                    instr[p3] = instr[p1] + instr[p2]
                elif opcode == 2:
                    instr[p3] = instr[p1] * instr[p2]
                elif opcode == 7:
                    instr[p3] = 1 if instr[p1] < instr[p2] else 0
                elif opcode == 8:
                    instr[p3] = 1 if instr[p1] == instr[p2] else 0
                pointer += 4

    return outputs[-1]

#soluzione 1
print(execute(data))

#soluzione 2
print(execute(data, 5))
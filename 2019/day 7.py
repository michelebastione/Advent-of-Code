from itertools import permutations

with open('input7.txt') as file:
    data = [*map(int, file.read().split(','))]

class Executer:
    def __init__(self, array, inps):
        self.array = [*array]
        self.inps = inps

    def execute(self):
        instr = self.array
        pointer = 0
        while True:
            to_exec = instr[pointer]
            if to_exec == 99:
                yield -1
                break

            temp = str(to_exec)
            opcode =  to_exec if len(temp) < 2 else int(temp[-2:])
            parameter_1 = 0 if len(temp) < 3 else int(temp[-3])
            parameter_2 = 0 if len(temp) < 4 else int(temp[-4])
            parameter_3 = 0 if len(temp) < 5 else 1

            p1 = (instr[pointer+1], pointer+1)[parameter_1]
            if opcode == 3:
                instr[p1] = self.inps[0]
                del self.inps[0]
                pointer += 2
            elif opcode == 4:
                yield instr[p1]
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

largest_signal = 0
for permutation in permutations([0,1,2,3,4]):
    phases = [*permutation]
    last_output = 0
    for phase in phases:
        gen_signal = Executer(data, [phase, last_output]).execute()
        last_output = next(gen_signal)
    largest_signal = max(largest_signal, last_output)

#soluzione 1
print(largest_signal)

largest_signal = 0
for permutation in permutations([5,6,7,8,9]):
    phases = [[perm] for perm in permutation]
    executers = [Executer(data, phase) for phase in phases]
    executers_gens = [exec.execute() for exec in executers]
    last_output = 0
    while True:
        for ampl in range(5):
            if last_output != -1:
                executers[ampl].inps.append(last_output)
            last_output = next(executers_gens[ampl])
        if last_output == -1:
            break
        largest_signal = max(largest_signal, last_output)

#soluzione 2
print(largest_signal)
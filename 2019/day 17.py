import numpy as np
from itertools import product

with open('input17.txt') as file:
    raw_data = file.read().split(',')
    data = [*map(int, raw_data)]

class Executer:
    def __init__(self, array, inputs=[]):
        self.array = [*array]+[0]*3000
        self.inputs = inputs

    def execute(self):
        instr = self.array
        pointer = 0
        relative_base = 0
        while True:
            to_exec = instr[pointer]
            if to_exec == 99:
                break

            temp = str(to_exec)
            opcode =  to_exec if len(temp) < 2 else int(temp[-2:])
            parameter_1 = 0 if len(temp) < 3 else int(temp[-3])
            parameter_2 = 0 if len(temp) < 4 else int(temp[-4])
            parameter_3 = 0 if len(temp) < 5 else int(temp[-5])

            p1 = (instr[pointer+1], pointer+1, relative_base+instr[pointer+1])[parameter_1]
            if opcode == 3:
                instr[p1] = self.inputs.pop(0)
                pointer += 2
            elif opcode == 4:
                yield instr[p1]
                pointer += 2
            elif opcode == 9:
                relative_base += instr[p1]
                pointer += 2
            else:
                p2 = (instr[pointer+2], pointer+2, relative_base+instr[pointer+2])[parameter_2]
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
                    p3 = (instr[pointer+3], pointer+3, relative_base+instr[pointer+3])[parameter_3]
                    if opcode == 1:
                        instr[p3] = instr[p1] + instr[p2]
                    elif opcode == 2:
                        instr[p3] = instr[p1] * instr[p2]
                    elif opcode == 7:
                        instr[p3] = 1 if instr[p1] < instr[p2] else 0
                    elif opcode == 8:
                        instr[p3] = 1 if instr[p1] == instr[p2] else 0
                    pointer += 4

def is_cross(arr, r, c):
    return np.all(arr[r-1: r+2, c] == arr[r, c-1: c+2])

raw_scaffolds = ''
for e in Executer(data).execute():
    raw_scaffolds += chr(e)
scaffolds = np.array([[*line] for line in raw_scaffolds.splitlines()][:-1]) == '#'

minor = lambda x: range(1, x-1)
inner_grid = product(*map(minor, scaffolds.shape))

#soluzione 1
print(
    sum(
        r * c for r, c in inner_grid
        if np.all(scaffolds[r-1: r+2, c]) and np.all(scaffolds[r, c-1: c+2])
    )
)


# path calculated by hand: R,6,L,12,R,6,R,6,L,12,R,6,L,12,R,6,L,8,L,12,R,12,L,10,L,10,L,12,R,6,L,8,L,12,
#                          R,12,L,10,L,10,L,12,R,6,L,8,L,12,R,12,L,10,L,10,L,12,R,6,L,8,L,12,R,6,L,12,R,6

A = 'R,6,L,12,R,6\n'
B = 'L,12,R,6,L,8,L,12\n'
C = 'R,12,L,10,L,10\n'
path_parametrized = 'A,A,B,C,B,C,B,C,B,A\n'
video_feed = 'n\n'
joined_input = path_parametrized + A + B + C + video_feed

#soluzione 2
data[0] = 2
for out in Executer(data, [ord(k) for k in joined_input]).execute():
    pass
print(out)
from itertools import product

with open('input19.txt') as file:
    data = [*map(int, file.read().split(','))]

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

def is_attracted(x, y):
    beam = Executer(data, [x,y])
    return next(beam.execute())

#soluzione 1
print(
    sum(
        is_attracted(*p) for p in product(range(50), repeat=2)
        )
     )

x0, y0 = 300, 500

while True:
    while not is_attracted(x0, y0):
        x0 += 1
    x1 = x0
    while is_attracted(x1, y0):
        x1 += 1
    if x1 - x0 >= 100:
        break
    y0 += 1

check = True
while check:
    while is_attracted(x0, y0) and is_attracted(x0+99, y0):
        if is_attracted(x0, y0+99):
            check = False
            break
        x0 += 1
    y0 += 1

#soluzione 2
print(x0*10000 + y0-1)
import numpy as np

with open('input11.txt') as file:
    data = [*map(int, file.read().split(','))]

class Executer:
    def __init__(self, array, inputs=[]):
        self.array = [*array]+[0]*1000
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
                instr[p1] = self.inputs[0]
                del self.inputs[0]
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

def turn(instr, orientation, pos):
    new_direction = -1 if instr else 1
    to_exec = {
        i:
            f"pos[{not i % 2}] {'-' if i//2 else '+'}= {new_direction}"
        for i in range(4)
    }
    exec(to_exec[orientation])
    return (orientation + new_direction) % 4

robo_painter = Executer(data, [0])
correct_robo_painter = Executer(data, [1])

def paint(painter):
    steps = painter.execute()
    tiles = {(0, 0): 0}
    current_cell = [0, 0]
    orientation = 0

    for step in steps:
        tiles[tuple(current_cell)] = step
        direction = next(steps)
        orientation = turn(direction, orientation, current_cell)
        t = tuple(current_cell)
        if t not in tiles:
            tiles[t] = 0
        painter.inputs.append(tiles[tuple(current_cell)])

    painter.panels_painted = len(tiles)
    return tiles

#soluzione 1
paint(robo_painter)
print(robo_painter.panels_painted)

#soluzione 2
reg_code = paint(correct_robo_painter)
graph = np.array([['.']*43]*6)
for i in reg_code:
    x, y = [i[0], -i[1]]
    graph[x, y] = '#' if reg_code[i] else '.'

for row in graph:
    print(*(row))
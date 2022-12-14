import asyncio, re
from itertools import combinations

with open('input25.txt') as file:
    data = [*map(int, file.read().split(','))]

class Executer:
    def __init__(self, array, inputs=[]):
        self.array = [*array]+[0]*1000
        self.inputs = inputs

#   async def per giocare al gioco
    def execute(self):
        instr = self.array
        pointer = 0
        relative_base = 0
        inps = self.ainput()
        to_print = ''
        printer_ready = False
        while True:
            to_exec = instr[pointer]
            if to_exec == 99:
                print(re.search(r'\d+', to_print.split('\n')[-2]).group())
                break

            temp = str(to_exec)
            opcode =  to_exec if len(temp) < 2 else int(temp[-2:])
            parameter_1 = 0 if len(temp) < 3 else int(temp[-3])
            parameter_2 = 0 if len(temp) < 4 else int(temp[-4])
            parameter_3 = 0 if len(temp) < 5 else int(temp[-5])

            p1 = (instr[pointer+1], pointer+1, relative_base+instr[pointer+1])[parameter_1]
            if opcode == 3:
                to_print = ''
                printing = False
                if len(self.inputs) == 0:
#                    self.inputs = await self.ainputs()
#                    cancellare la riga sottostante se si vuole giocare
                    for i in inps:
                        self.inputs.append(i)
                instr[p1] = self.inputs[0]
                del self.inputs[0]
                pointer += 2
            elif opcode == 4:
                #print(chr(instr[p1]), end='')
                char = chr(instr[p1])
                to_print += char
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

#   async def nel caso in cui si voglia "giocarlo"
    def ainput(self):
#        instruction = input('Waiting for input: ')
#        return [ord(j) for j in instruction] + [10]
        for instr in ['north', 'north', 'take space heater', 'east', 'take semiconductor', 'west', 'south',
                     'south', 'east', 'take ornament', 'south', 'take festive hat', 'east', 'take asterisk',
                     'south', 'east', 'take cake', 'west', 'west', 'take food ration', 'east',
                     'north','west', 'north', 'west', 'west', 'north', 'north', 'inv']:
            for i in instr:
                yield ord(i)
            yield 10
        items = ['cake', 'space heater', 'ornament', 'asterisk', 
                 'festive hat', 'food ration', 'semiconductor']
        for j in range(4, 7):
            for combination in combinations(items, j):
                for item in items:
                    command = f'drop {item}\n'
                    for c in command:
                        yield ord(c)
                comb = [*combination]
                for co in comb:
                    command = f'take {co}\n'
                    for c in command:
                        yield ord(c)
                for w in 'west\n':
                    yield ord(w)

#
droid = Executer(data)
droid.execute()
#loop = asyncio.get_event_loop()
#task = loop.create_task(droid.execute())
#loop.run_until_complete(task)

import re, asyncio

with open('input18.txt') as file:
    data = file.read().splitlines()

def duet(instructions):
    pointer = 0
    registers = {i.split()[1]: 0 for i in instructions}

    while 0 <= pointer < len(data):
        instr = data[pointer].split()
        check = registers[instr[1]] if instr[1].isalpha() else int(instr[1])
        if len(instr) == 3:
            value = registers[instr[2]] if instr[2].isalpha() else int(instr[2])

        if instr[0] == 'snd':
            frequency = check
        elif instr[0] == 'rcv':
            if check != 0:
                return frequency
        elif instr[0] == 'jgz':
            pointer += value-1 if check > 0 else 0
        else:
            to_exec = {'set': '=', 'add': '+=', 'mul': '*=', 'mod': '%='}
            exec(f"registers[instr[1]] {to_exec[re.search(r'set|add|mul|mod', instr[0]).group(0)]} value")

        pointer += 1

#soluzione 1
print(duet(data))

regs1 =  {i.split()[1]: 0 for i in data}
regs2 = {i.split()[1]: 0 for i in data}
regs2['p'] = 1

q1 = []
q2 = []

async def async_duet(instructions, registers, queue1, queue2):
    pointer = 0
    counter = 0
    while 0 <= pointer < len(data):
        instr = data[pointer].split()
        check = registers[instr[1]] if instr[1].isalpha() else int(instr[1])
        if len(instr) == 3:
            value = registers[instr[2]] if instr[2].isalpha() else int(instr[2])

        if instr[0] == 'snd':
            queue2.append(check)
            counter += 1
        elif instr[0] == 'rcv':
            if len(queue1)==0 and len(queue2)==0:
                if queue1 is q2:
                    return counter
                break
            while len(queue1) == 0:
                if len(queue2) == 0:
                    return 'terminated'
                await asyncio.sleep(0)
            registers[instr[1]] = queue1[0]
            del queue1[0]
        elif instr[0] == 'jgz':
            pointer += value-1 if check > 0 else 0
        else:
            to_exec = {'set': '=', 'add': '+=', 'mul': '*=', 'mod': '%='}
            exec(f"registers[instr[1]] {to_exec[re.search(r'set|add|mul|mod', instr[0]).group(0)]} value")

        pointer += 1
    return

#soluzione 2
loop = asyncio.get_event_loop()
t1 = loop.create_task(async_duet(data, regs1, q1, q2))
t2 = loop.create_task(async_duet(data, regs2, q2, q1))
print(loop.run_until_complete(asyncio.gather(t1, t2)))
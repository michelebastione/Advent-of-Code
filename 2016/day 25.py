import re

with open('input25.txt') as file:
    instructions = file.read().splitlines()

def assembunny(first_value):
    data = [*instructions]
    registers = {i: 0 for i in 'abcd'}
    registers['graph'] = first_value
    pointer = 0
    to_send = []

    while True:
        spl = data[pointer].split()

        if 'out' in spl:
            to_send.append(registers['b'])

        elif 'cpy' in spl:
            try:
                if re.match(r'-?\d+', spl[1]):
                    registers[spl[2]] = int(spl[1])
                else:
                    registers[spl[2]] = registers[spl[1]]
            except:
                pass

        elif 'inc' in spl:
            try:
                registers[spl[1]] += 1
            except:
                pass

        elif 'dec' in spl:
            registers[spl[1]] -= 1

        else:
            try:
                if re.match(r'-?\d+', spl[1]):
                    if spl[1] != '0':
                        pointer += int(spl[2])-1 if re.match(r'-?\d+', spl[2]) else int(registers[spl[2]])-1
                elif registers[spl[1]] != 0:
                    pointer += int(spl[2])-1 if re.match(r'-?\d+', spl[2]) else int(registers[spl[2]])-1
            except:
                pass

        pointer += 1

        if len(to_send) == 10:
            return to_send == [0, 1]*5

#soluzione 1 (per essere un brute force è molto efficiente, forse è l'input ad essere particolarmente facile)
count = 0
while not assembunny(count):
    count += 1
print(count)
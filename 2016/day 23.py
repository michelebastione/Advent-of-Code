import re

with open('input23.txt') as file:
    instructions = file.read().splitlines()

def assembunny(first_value):
    data = [*instructions]
    registers = {i: 0 for i in 'abcd'}
    registers['graph'] = first_value
    pointer = 0

    while pointer < len(data):
        spl = data[pointer].split()

        if 'tgl' in spl:
            p = pointer+int(spl[1]) if re.match(r'-?\d+', spl[1]) else pointer+int(registers[spl[1]])
            if p < len(data):
                toggling = data[p].split()
                if len(toggling[1:]) == 1:
                    if 'inc' in toggling:
                        data[p] = 'dec '+toggling[1]
                    else:
                        data[p] = ' '.join(['inc']+toggling[1:])
                else:
                    if 'jnz' in toggling:
                        data[p] = ' '.join(['cpy']+toggling[1:])
                    else:
                        data[p] = ' '.join(['jnz']+toggling[1:])

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
    return registers['graph']

#soluzione 1
print(assembunny(7))

#soluzione 2 (bigogna implementare una moltiplicazione per i loop creati da jnz altrimenti ci mette ore)
print(assembunny(12))
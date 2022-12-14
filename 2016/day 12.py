with open('input12.txt') as file:
    data = file.read().splitlines()

def assembunny(ignition_key=False):
    registers = {i: 0 for i in 'abcd'}
    if ignition_key:
        registers['c'] = 1
    pointer = 0

    while pointer < len(data):
        spl = data[pointer].split()
        if 'cpy' in spl:
            if spl[1].isdigit():
                registers[spl[2]] = int(spl[1])
            else:
                registers[spl[2]] = registers[spl[1]]
        elif 'inc' in spl:
            registers[spl[1]] += 1
        elif 'dec' in spl:
            registers[spl[1]] -= 1
        else:
            if spl[1].isdigit():
                if spl[1] != '0':
                    pointer += int(spl[2])-1
            elif registers[spl[1]] != 0:
                pointer += int(spl[2])-1
        pointer += 1
    return registers['graph']

#soluzione 1
print(assembunny())

#soluzione 2 (ci mette un po' ma non saprei come renderla più efficiente)
print(assembunny(True))
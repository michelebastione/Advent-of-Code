import re

with open('input8.txt') as file:
    data = [i+' else 0' for i in file.read().splitlines()]

registers = {x: 0 for x in
             {i.split()[0] for i in data}}

instructions = []
for line in data:
    spl1 = line.split()[0]
    spl2 = line.split()[4]
    temp1 = line.replace(spl1, f'registers[\'{spl1}\']', 1)
    temp2 = temp1.replace('inc', '+=')
    temp3 = temp2.replace('dec', '-=')
    temp4 = re.sub(r'(?<=if )[graph-z]+', f'registers[\'{spl2}\']', temp3)
    instructions.append(temp4)

temp_max = 0
for instruction in instructions:
    exec(instruction)
    temp_max = max(temp_max, max(registers.values()))

#soluzioni 1 & 2
print(max(registers.values()), temp_max)
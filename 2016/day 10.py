import re
from copy import deepcopy

with open('input10.txt') as file:
    data = file.read().splitlines()

holding = dict()
output_bins = dict()
instructions = dict()
for line in data:
    if 'output' in line:
        output_bins[int(re.search(r'(?<=output )\d+', line).group(0))] = 0
    if 'value' in line:
        value, bot = map(int, re.findall(r'\d+', line))
        if bot in holding:
            holding[bot].append(value)
        else:
            holding[bot] = [value]
    else:
        instructions[int(re.search(r'\d+', line).group(0))] = line.split('gives ')[1]

first_solution = True
while not (output_bins[0] and output_bins[1] and output_bins[2]):
    copy = deepcopy(holding)
    for bot in copy:
        values = holding[bot]
        instruction = instructions[bot]
        if len(values) == 2:
            minn, maxx = sorted(values)
            if minn == 17 and maxx == 61:
                if first_solution:

                    #soluzione 1
                    print(bot)
                    first_solution = False

            out1, out2 = map(int, re.findall(r'\d+', instruction))
            if 'low to output' in instruction:
                output_bins[out1] = minn
                if out2 in holding:
                    holding[out2].append(maxx)
                else:
                    holding[out2] = [maxx]
            elif 'high to output' in instruction:
                output_bins[out2] = maxx
                if out1 in holding:
                    holding[out1].append(minn)
                else:
                    holding[out1] = [minn]
            else:
                if out1 in holding:
                    holding[out1].append(minn)
                else:
                    holding[out1] = [minn]
                if out2 in holding:
                    holding[out2].append(maxx)
                else:
                    holding[out2] = [maxx]
            del values[0]
            del values[0]

#soluzione 2
print(output_bins[0] * output_bins[1] * output_bins[2])
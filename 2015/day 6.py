import numpy as np
import re

with open('input6.txt') as file:
    instructions = file.read().splitlines()

lights = np.zeros((1000,1000), dtype=bool)
for instruction in instructions:
    match = re.findall(r'\d+,\d+', instruction)
    sep = [match[0].split(','), match[1].split(',')]
    coord = [[int(sep[0][0]), int(sep[1][0])+1],
             [int(sep[0][1]), int(sep[1][1])+1]]
    if 'on' in instruction:
        lights[coord[0][0]:coord[0][1],coord[1][0]:coord[1][1]] = True
    elif 'off' in instruction:
        lights[coord[0][0]:coord[0][1],coord[1][0]:coord[1][1]] = False
    else:
        lights[coord[0][0]:coord[0][1],coord[1][0]:coord[1][1]] = np.logical_not(lights[coord[0][0]:coord[0][1],coord[1][0]:coord[1][1]])

#soluzione 1
print(np.sum(lights))

lights = np.zeros((1000,1000))
for instruction in instructions:
    match = re.findall(r'\d+,\d+', instruction)
    sep = [match[0].split(','), match[1].split(',')]
    coord = [[int(sep[0][0]), int(sep[1][0])+1],
             [int(sep[0][1]), int(sep[1][1])+1]]
    if 'on' in instruction:
        lights[coord[0][0]:coord[0][1],coord[1][0]:coord[1][1]] += 1
    elif 'off' in instruction:
        lights[coord[0][0]:coord[0][1],coord[1][0]:coord[1][1]] = np.where(lights[coord[0][0]:coord[0][1],coord[1][0]:coord[1][1]] > 0,
                                                                           lights[coord[0][0]:coord[0][1],coord[1][0]:coord[1][1]]-1, 0)
    else:
        lights[coord[0][0]:coord[0][1],coord[1][0]:coord[1][1]] += 2
        
#soluzione 2
print(int(np.sum(lights)))

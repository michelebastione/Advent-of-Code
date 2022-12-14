import numpy as np
from copy import deepcopy

with open('input17.txt') as file:
    config = np.array([[i for i in line] for line in file.read().splitlines()])

cubes = np.array([[['.']*22]*22]*15)

cubes[7,7:15,7:15]=config

def cycle(array, repeat):
    temp = deepcopy(array)
    for r in range(repeat):
        for z in range(1,14):
            for x in range(1,21):
                for y in range(1,21):
                    adjacent = array[z-1:z+2,x-1:x+2,y-1:y+2]
                    count = len(np.where(adjacent=='#')[0])
                    if array[z,x,y]=='#':
                        if count<3 or count>4:
                            temp[z,x,y]='.'
                    elif count==3:
                        temp[z,x,y]='#'      
        array = deepcopy(temp)
    return len(np.where(temp=='#')[0])

#soluzione 1
print(cycle(cubes,6))

hcubes = np.array([[[['.']*22]*22]*15]*15)
hcubes[7,7,7:15,7:15]=config

def hcycle(array, repeat):
    temp = deepcopy(array)
    for r in range(repeat):
        for w in range(1,14):
            for z in range(1,14):
                for x in range(1,21):
                    for y in range(1,21):
                        adjacent = array[w-1:w+2,z-1:z+2,x-1:x+2,y-1:y+2]
                        count = len(np.where(adjacent=='#')[0])
                        if array[w,z,x,y]=='#':
                            if count<3 or count>4:
                                temp[w,z,x,y]='.'
                        elif count==3:
                            temp[w,z,x,y]='#'      
        array = deepcopy(temp)
    return len(np.where(temp=='#')[0])

#soluzione 2
print(hcycle(hcubes,6))

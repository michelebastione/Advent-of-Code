with open('input1.txt') as file:
    instr = [(line[0], int(line[1:])) for line in file.read().split(', ')]
print(instr)
def move(n, orientation, current):
    if n%2 == 0:
        if orientation:
            if instr[n][0] == 'L':
                current[0] -= instr[n][1]
                orientation = 0
            else:
                current[0] += instr[n][1]
        else:
            if instr[n][0] == 'R':
                current[0] -= instr[n][1]
            else:
                current[0] += instr[n][1]
                orientation = 1
    else:
        if orientation:
            if instr[n][0] == 'R':
                current[1] -= instr[n][1]
                orientation = 0
            else:
                current[1] += instr[n][1]
        else:
            if instr[n][0] == 'L':
                current[1] -= instr[n][1]
            else:
                current[1] += instr[n][1]
                orientation = 1
    return orientation

def move_one_step(n, orientation, current):
    all_coord = []
    if n%2 == 0:
        if orientation:
            if instr[n][0] == 'L':
                for i in range(instr[n][1]):
                    current[0] -= 1
                    all_coord.append([*current])
                orientation = 0
            else:
                for i in range(instr[n][1]):
                    current[0] += 1
                    all_coord.append([*current])
        else:
            if instr[n][0] == 'R':
                for i in range(instr[n][1]):
                    current[0] -= 1
                    all_coord.append([*current])
            else:
                for i in range(instr[n][1]):
                    current[0] += 1
                    all_coord.append([*current])
                orientation = 1
    else:
        if orientation:
            if instr[n][0] == 'R':
                for i in range(instr[n][1]):
                    current[1] -= 1
                    all_coord.append([*current])
                orientation = 0
            else:
                for i in range(instr[n][1]):
                    current[1] += 1
                    all_coord.append([*current])
        else:
            if instr[n][0] == 'L':
                for i in range(instr[n][1]):
                    current[1] -= 1
                    all_coord.append([*current])
            else:
                for i in range(instr[n][1]):
                    current[1] += 1
                    all_coord.append([*current])
                orientation = 1
    return all_coord, orientation


current_coord = [0, 0]
orientation = 1

#soluzione 1
for i in range(len(instr)):
    orientation = move(i, orientation, current_coord)
print(abs(current_coord[0]) + abs(current_coord[1]))

current_coord = [0, 0]
coords = []
orientation = 1
check, i = True, 0

#soluzione 2 (implementazione vomitevole ma funziona)
while check:
    result = move_one_step(i, orientation, current_coord)
    coords += result[0]
    orientation = result[1]
    for j in coords:
        if coords.count(j) > 1:
            check = False
            print(abs(j[0]) + abs(j[1]))
            break
    i += 1
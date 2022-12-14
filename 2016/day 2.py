with open('input2.txt') as file:
    directions = file.read().splitlines()

keypad = [[1,2,3], [4,5,6], [7,8,9]]
prev = [1,1]
code = []

for line in directions:
    for direction in line:
        if direction == 'U':
            prev[0] -= 0 if prev[0] == 0 else 1
        if direction == 'D':
            prev[0] += 0 if prev[0] == 2 else 1
        if direction == 'R':
            prev[1] += 0 if prev[1] == 2 else 1
        if direction == 'L':
            prev[1] -= 0 if prev[1] == 0 else 1
    code.append(keypad[prev[0]][prev[1]])

#soluzione 1
print(''.join([str(i) for i in code]))

strange_code = []
strange_keypad = [[0,0,1,0,0], [0,2,3,4,0], [5,6,7,8,9], [0,'A','B','C',0], [0,0,'D',0,0]]
possible = [[0,2],
            [1,1], [1,2], [1,3],
            [2,0], [2,1], [2,2], [2,3], [2,4],
            [3,1], [3,2], [3,3],
            [4,2]]
prev = [2,2]

for line in directions:
    for direction in line:
        if direction == 'U':
            temp = [prev[0]-1, prev[1]]
            if temp in possible:
                prev = temp
        if direction == 'D':
            temp = [prev[0]+1, prev[1]]
            if temp in possible:
                prev = temp
        if direction == 'R':
            temp = [prev[0], prev[1]+1]
            if temp in possible:
                prev = temp
        if direction == 'L':
            temp = [prev[0], prev[1]-1]
            if temp in possible:
                prev = temp
    strange_code.append(strange_keypad[prev[0]][prev[1]])

#soluzione 2
print(''.join([str(j) for j in strange_code]))
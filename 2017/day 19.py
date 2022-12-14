import numpy as np

with open('input19.txt') as file:
    data = np.array([[*line[1: -1]] for line in file.read().splitlines()[:-1]])

x, y = 0, np.where(data[0] == '|')[0][0]
direction = 2

def adjacent(i, j, dir):
    choices = {}
    if i > 0:
        choices[0] = (i-1, j)
    if i < len(data)-1:
        choices[2] = (i+1, j)
    if j > 0:
        choices[3] = (i, j-1)
    if j < len(data[0])-1:
        choices[1] = (i, j+1)

    if dir in choices:
        del choices[dir]
    opp = (dir+2) % 4
    if opp in choices:
        del choices[opp]

    return choices

path = ''
count = 0

while True:
    count += 1
    s = data[x, y]
    if s == '+':
        adj = adjacent(x, y, direction)
        for a, c in adj.items():
            val = data[c]
            if val != ' ':
                direction, x, y = a, *c

    else:
        update = {0: 'x -= 1', 2: 'x += 1', 3: 'y -= 1', 1: 'y += 1'}
        exec(update[direction])
        if s.isalpha():
            path += s
            if data[x, y] == ' ':
                break

#soluzioni 1 & 2
print(path, count)
with open('input2.txt') as file:
    instr = [(line[0], int(line.split()[1])) for line in file.read().splitlines()]

# soluzione 1
x, y, = 0, 0
for i in instr:
    if i[0] == "f":
     x += i[1]
    elif i[0] == "d":
     y += i[1]
    else:
     y -= i[1]
print(x*y)

# soluzione 2
x, y, aim = 0, 0, 0
for j in instr:
    if j[0] == "f":
     x += j[1]
     y += aim*j[1]
    elif j[0] == "d":
     aim += j[1]
    else:
     aim -=j[1]
print(x*y)
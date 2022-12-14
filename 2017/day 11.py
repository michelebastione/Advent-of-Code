with open('input11.txt') as file:
    data = file.read().split(',')

def to_cube(r, c):
    x = c
    z = r - c//2
    y = -x-z
    return x, y, z

def distance_from_origin(hex):
    return sum(abs(i) for i in hex)//2


x, y = 0, 0
furthest = 0
for i in data:
    if i == 'n':
        x -= 1
    if i == 's':
        x += 1
    if i == 'nw':
        y -= 1
        x -= 1 if y % 2 == 0 else 0
    if i == 'sw':
        y -= 1
        x += 0 if y % 2 == 0 else 1
    if i == 'ne':
        y += 1
        x -= 1 if y % 2 == 0 else 0
    if i == 'se':
        y += 1
        x += 0 if y % 2 == 0 else 1
    furthest = max(furthest, distance_from_origin(to_cube(x, y)))

#soluzioni 1 & 2 (ho consultato una guida per sistemi di coordinate su griglie esagonali)
print(distance_from_origin(to_cube(x, y)), furthest)
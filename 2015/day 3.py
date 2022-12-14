with open('input3.txt') as file:
    data = file.read()

def move(directions):
    
    grid_position = [0,0]
    coordinates = {(0,0)}

    for instruction in directions:
        if instruction == '>':
            grid_position[0] += 1
        if instruction == '<':
            grid_position[0] -= 1
        if instruction == '^':
            grid_position[1] += 1
        if instruction == 'v':
            grid_position[1] -= 1
        coordinates.add(tuple(grid_position))

    return coordinates

print(len(move(data)))
print(len(move(data[::2]).union(move(data[1::2]))))

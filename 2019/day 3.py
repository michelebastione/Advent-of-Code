with open('input3.txt') as file:
    lines = file.read().splitlines()
    wire1 = lines[0].split(',')
    wire2 = lines[1].split(',')

manhattan_distance = lambda x: abs(x[0]) + abs(x[1])

def path(instructions, trace_steps=None):
    coordinates = set()
    current_x, current_y = 0, 0
    for instruction in instructions:
        direction = instruction[0]
        value = int(instruction[1:])
        if direction in 'RL':
            copy_x = current_x
            if direction == 'R':
                current_x += value
                temp_coords = range(copy_x+1, current_x+1)
            else:
                current_x -= value
                temp_coords = range(current_x+1, copy_x+1)
            coordinates.update((i, current_y) for i in temp_coords)
        else:
            copy_y = current_y
            if direction == 'U':
                current_y += value
                temp_coords = range(copy_y+1, current_y+1)
            else:
                current_y -= value
                temp_coords = range(current_y+1, copy_y+1)
            coordinates.update((current_x, i) for i in temp_coords)
        if trace_steps in coordinates:
            coordinates.add((current_x, current_y))
            return len(coordinates) - abs(current_x-trace_steps[0]) - abs(current_y-trace_steps[1])
    return coordinates

path1 = path(wire1)
path2 = path(wire2)
crossed_paths = path1.intersection(path2)

#soluzione 1
print(manhattan_distance(min(crossed_paths, key=manhattan_distance)))

#soluzione 2
print(min(path(wire1, i)+path(wire2, i) for i in crossed_paths))
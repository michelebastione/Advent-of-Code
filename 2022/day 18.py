with open('input18.txt') as file:
    cubes = [[*map(int, line.split(","))] for line in file]


def adjacent(x, y, z):
    return [
        [x+1, y, z],
        [x-1, y, z],
        [x, y+1, z],
        [x, y-1, z],
        [x, y, z+1],
        [x, y, z-1]
    ]


# solution 1
surface = 0
for cube in cubes:
    surface += sum(adj not in cubes for adj in adjacent(*cube))
print(surface)

prova="""R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
with open('input9.txt') as file:
    instructions = []
    for line in file:
        i, j = line.split()
        instructions.append((i, int(j)))


def rope(n):
    knots = [[0, 0] for _ in range(n)]
    head = knots[0]
    covered = {(0, 0)}
    for direction, magnitude in instructions:
        for _ in range(magnitude):
            if direction == "R":
                head[0] += 1
            elif direction == "L":
                head[0] -= 1
            elif direction == "U":
                head[1] += 1
            else:
                head[1] -= 1

            previous = head
            for knot in knots[1:]:
                if abs(previous[0] - knot[0]) > 1 or abs(previous[1] - knot[1]) > 1 or abs(sum(previous) - sum(knot)) > 2:
                    knot[0] += 1 if previous[0] > knot[0] else -1 if previous[0] < knot[0] else 0
                    knot[1] += 1 if previous[1] > knot[1] else -1 if previous[1] < knot[1] else 0
                previous = knot
            covered.add(tuple(knots[-1]))
    return len(covered)

# solution 1
print(rope(2))

# solution 2
print(rope(10))

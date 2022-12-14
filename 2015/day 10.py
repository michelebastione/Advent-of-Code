from itertools import groupby

def look_and_see(n):
    result = ''
    for i in groupby(n):
        a, b = i
        result += str(len([*b]))+a
    return result

puzzle_input = '1321131112'

for i in range(50):
    puzzle_input = look_and_see(puzzle_input)

    #soluzione 1
    if i == 39:
        print(len(puzzle_input))

#soluzione 2
print(len(puzzle_input))

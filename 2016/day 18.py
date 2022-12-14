with open('input18.txt') as file:
    starting_row = file.read()

def next_row(string):
    string = '.' + string + '.'
    result = ''
    for i in range(1, len(string)-1):
        result += '^' if string[i-1: i+2] in ['^^.', '.^^', '^..', '..^'] else '.'
    return result

def safe_tiles(current_row, n):
    total = 0
    for i in range(n):
        total += current_row.count('.')
        current_row = next_row(current_row)
    return total

#soluzioni 1 & 2
print(safe_tiles(starting_row, 40), safe_tiles(starting_row, 400000))
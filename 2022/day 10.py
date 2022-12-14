with open('input10.txt') as file:
    increments = []
    for line in file:
        to_add = [0] if "noop" in line else [0, int(line.split()[1])]
        increments.extend(to_add)

register = {}
total = 1
for cycle, value in enumerate(increments, 1):
    register[cycle] = total
    total += value

# solution 1
signal_strength = {cycle: cycle*value for cycle, value in register.items()}
print(sum(strength for cycle, strength in signal_strength.items() if (cycle-20)%40 == 0))

# solution 2
crt = [['.' for _ in range(40)] for _ in range(6)]
for cycle, position in register.items():
    line, pixel = divmod(cycle - 1, 40)
    if position-1 <= pixel <= position+1:
        crt[line][pixel] = "#"
print(*[''.join(line) for line in crt], sep='\n')

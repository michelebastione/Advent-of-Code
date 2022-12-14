with open('input20.txt') as file:
    data = []
    for line in file.read().splitlines():
        spl = line.split('-')
        data.append((int(spl[0]), int(spl[1])))

ranges = sorted(data, key=lambda x: x[0])
lowest_allowed = 0

#soluzione 1
for r1, r2 in ranges:
    if r1 <= lowest_allowed:
        lowest_allowed = max(lowest_allowed, r2+1)
    else:
        break
print(lowest_allowed)

#soluzione 2
last_step = 0
next_step = 0
total = 0
for r1, r2 in ranges:
    if r1 <= next_step:
        next_step = max(next_step, r2+1)
    else:
        total += next_step-last_step
        last_step = r1
        next_step = r2+1
total += next_step-last_step
print(2**32-total)

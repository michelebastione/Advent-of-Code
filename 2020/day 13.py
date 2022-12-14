from itertools import combinations

with open('input13.txt') as file:
    data = file.read().splitlines()
    time = int(data[0])
    schedule = data[1].split(',')
    buses = [int(bus) for bus in schedule if bus.isdigit()]

def prod(it):
    result = 1
    for i in it:
        result *= i
    return result

#soluzione 1
count = 0
check = True
while check:
    for bus in buses:
        if (count+time) % bus == 0:
            print(bus*count)
            check = False
            break
    count += 1

#soluzione 2
remainders = {19:0}
for timestamp in range(1, len(schedule)):
    if schedule[timestamp].isdigit():
        t = int(schedule[timestamp])
        remainders[t] = t-timestamp if timestamp < t else t-(timestamp % t)

N = prod(remainders)
Ni = [prod(combination) for combination in combinations(remainders, len(remainders)-1)][::-1]
yi = []

for i in range(len(Ni)):
    c = 0
    while (Ni[i]*c) % list(remainders.keys())[i] != 1:
        c += 1
    yi.append(c)
    
print(sum(list(remainders.values())[k]*Ni[k]*yi[k] for k in range(len(Ni))) % N)

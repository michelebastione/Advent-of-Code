from itertools import product

with open('input2.txt') as file:
    data = [*map(int, file.read().split(','))]

def execute(array, noun, verb):
    temp = [*array]
    temp[1] = noun
    temp[2] = verb
    for i in range(0, len(temp), 4):
        if temp[i] == 99:
            break
        elif temp[i] == 1:
            temp[temp[i+3]] = temp[temp[i+1]] + temp[temp[i+2]]
        elif temp[i] == 2:
            temp[temp[i+3]] = temp[temp[i+1]] * temp[temp[i+2]]
    return temp[0]

#soluzione 1
print(execute(data, 12, 2))

#soluzione 2
for p in product(range(100), repeat=2):
    if execute(data, p[0], p[1]) == 19690720:
        print(100*p[0] + p[1])
        break

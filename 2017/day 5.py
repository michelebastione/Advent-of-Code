with open('input5.txt') as file:
    data = [int(i) for i in file.read().splitlines()]

count = 0
pointer = 0
instructions = [*data]
while pointer < len(instructions):
    count += 1
    try:
        temp = instructions[pointer]
        instructions[pointer] += 1
        pointer += temp
    except:
        pass

#soluzione 1
print(count)

count = 0
pointer = 0
while pointer < len(data):
    count += 1
    try:
        temp = data[pointer]
        if data[pointer] >= 3:
            data[pointer] -= 1
        else:
            data[pointer] += 1
        pointer += temp
    except:
        pass

#soluzione 2
print(count)
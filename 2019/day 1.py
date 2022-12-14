with open('input1.txt') as file:
    data = [*map(int, file.read().splitlines())]

#soluzione 1
print(sum(x//3-2 for x in data))

total = 0
for i in data:
    subtotal = i//3-2
    while subtotal > 0:
        total += subtotal
        subtotal //= 3
        subtotal -= 2

#soluzione 1
print(total)
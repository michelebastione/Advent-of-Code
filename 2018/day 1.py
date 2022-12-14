with open('input1.txt') as file:
    data = [int(i) for i in file.read().splitlines()]

#soluzione 1
print(sum(data))

all_frequencies = []
current = 0
pointer = 0
while current not in all_frequencies:
    all_frequencies.append(current)
    current += data[pointer]
    pointer += 1; pointer %= len(data)

#soluzione 2 (implementazione lentissima, da rivedere possibilmente)
print(current)
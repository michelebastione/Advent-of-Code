with open('input4.txt') as file:
    pairs = []
    for line in file.read().splitlines():
        raw_pair = line.split(',')
        elf1 = [*map(int, raw_pair[0].split('-'))]
        elf2 = [*map(int, raw_pair[1].split('-'))]
        pairs.append([elf1, elf2])

# solution 1
contained_pairs = 0
for pair1, pair2 in pairs:
    if (pair1[0] <= pair2[0] and pair1[1] >= pair2[1]) or (pair1[0] >= pair2[0] and pair1[1] <= pair2[1]):
        contained_pairs += 1
print(contained_pairs)

# solution 2
overlapping_pairs = 0
for pair1, pair2 in pairs:
    if pair1[0] <= pair2[0] <= pair1[1] or pair2[0] <= pair1[0] <= pair2[1]:
        overlapping_pairs += 1
print(overlapping_pairs)

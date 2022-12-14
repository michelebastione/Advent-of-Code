with open('input19.txt') as file:
    combs, molecule = file.read().split('\n\n')

transformations = dict()
for line in combs.splitlines():
    transformation = line.split(' => ')
    if transformation[0] in transformations:
        transformations[transformation[0]].append(transformation[1])
    else:
        transformations[transformation[0]] = [transformation[1]]

molecules = set()
for transformation in transformations:
    for each in transformations[transformation]:
        start = 0
        for _ in range(molecule.count(transformation)):
            index = start + molecule[start:].index(transformation)
            start = index+len(transformation)
            temp = molecule[:index] + each + molecule[start:]
            molecules.add(temp)

#soluzione 1
print(len(molecules))

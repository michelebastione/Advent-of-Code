import numpy as np

with open('input21.txt') as file:
    lines = file.read().splitlines()
data = [line.split(' => ') for line in lines]

def all_rotations(array):
    result = []
    for i in range(4):
        rot = np.rot90(array, i)
        result.extend([rot, np.fliplr(rot)])
    return result

def to_array(s):
    return np.array([[i for i in j] for j in s.split('/')])

def stringfy(array):
    s = ''
    for i in array:
        s += ''.join(i) + '/'
    return s.strip('/')

rules = dict()
for before, after in data:
    for r in all_rotations(to_array(before)):
        rules[stringfy(r)] = to_array(after)

def join_arrays(arrays):
    l = int(len(arrays) ** 0.5)
    if l == 1:
        return arrays[0]
    final = np.concatenate((arrays[:l]), axis=1)
    for i in range(1, l):
        new = np.concatenate((arrays[i*l: (i+1)*l]), axis=1)
        final = np.concatenate((final, new))
    return final

pattern = to_array(".#./..#/###")

for k in range(18):
    d = 2 if len(pattern) % 2 == 0 else 3
    r = range(0, len(pattern), d)
    minors = [pattern[i: i+d, j: j+d] for i in r for j in r]
    transformed = [*map(lambda x: rules[stringfy(x)], minors)]
    pattern = join_arrays(transformed)
    if k == 4:
        print(np.count_nonzero(pattern == '#'))

#soluzione 2 (leggermente lenta ma decisamente abbordabile)
print(np.count_nonzero(pattern == '#'))
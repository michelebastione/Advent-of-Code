import re
from collections import deque

with open('input21.txt') as file:
    data = file.read().splitlines()

to_scramble = 'abcdefgh'
to_unscramble = 'fbgdceah'
swap = lambda s, i1, i2: s[: i1]+s[i2]+s[i1+1: i2]+s[i1]+s[i2+1: ]
reverse = lambda s, i1, i2 : s[: i1]+s[i1: i2+1][::-1]+s[i2+1:]

def move(s, i1, i2):
    l = list(s)
    temp = l.pop(i1)
    l.insert(i2, temp)
    return ''.join(l)

def rotate(s, i, dependent=False):
    temp = deque(s)
    if dependent:
        temp.rotate(i+1 if i<4 else i+2)
    else:
        temp.rotate(i)
    return ''.join(temp)

#soluzione 1
for line in data:
    if 'swap' in line:
        if 'position' in line:
            indices = sorted(map(int, re.findall(r'\d', line)))
        else:
            letters = re.findall(r'(?<=letter )[graph-h]', line)
            indices = sorted(map(to_scramble.index, letters))
        to_scramble = swap(to_scramble, *indices)

    if 'rotate' in line:
        if 'based' in line:
            based = True
            index = to_scramble.index(re.search(r'(?<=letter )[graph-h]', line).group(0))
        else:
            based = False
            index_raw = int(re.search(r'\d', line).group(0))
            index = -index_raw if 'left' in line else index_raw
        to_scramble = rotate(to_scramble, index, based)

    if 'move' in line:
        indices = map(int, re.findall(r'\d', line))
        to_scramble = move(to_scramble, *indices)

    if 'reverse' in line:
        indices = map(int, re.findall(r'\d', line))
        to_scramble = reverse(to_scramble, *indices)
print(to_scramble)

#soluzione 2
for line in data[::-1]:
    if 'swap' in line:
        if 'position' in line:
            indices = sorted(map(int, re.findall(r'\d', line)))
        else:
            letters = re.findall(r'(?<=letter )[graph-h]', line)
            indices = sorted(map(to_unscramble.index, letters))
        to_unscramble = swap(to_unscramble, *indices)

    if 'rotate' in line:
        if 'based' in line:
            index_raw = to_unscramble.index(re.search(r'(?<=letter )[graph-h]', line).group(0))
            index = {1: -1, 3: -2, 5: -3, 7: -4, 2: 2, 4: 1, 6: 0, 0: -1}[index_raw]
        else:
            index_raw = int(re.search(r'\d', line).group(0))
            index = -index_raw if 'right' in line else index_raw
        to_unscramble = rotate(to_unscramble, index)

    if 'move' in line:
        indices = map(int, re.findall(r'\d', line)[::-1])
        to_unscramble = move(to_unscramble, *indices)

    if 'reverse' in line:
        indices = map(int, re.findall(r'\d', line))
        to_unscramble = reverse(to_unscramble, *indices)
print(to_unscramble)


# 0-1
# 1-3
# 2-5
# 3-7
# 4-2
# 5-4
# 6-6
# 7-0
from itertools import product
from collections import deque

def xor(elements):
    final = 0
    for e in elements:
        final ^= e
    return final

def knot_raw(lengths, repeat=1):
    lst = deque(range(256))
    current = skip = 0
    for _ in range(repeat):
        for length in lengths:
            lst.rotate(-current)
            temp = list(lst)
            lst = deque(temp[:length][::-1]+temp[length:])
            lst.rotate(current)
            current = (current+length+skip) % 256
            skip += 1
    return lst

def knot_hash(string):
    c = s = 0
    new_lenghts = [ord(i) for i in string] + [17, 31, 73, 47, 23]
    sparse = knot_raw(new_lenghts, 64)
    dense = [xor(list(sparse)[n: n+16]) for n in range(0, 256, 16)]
    hexes = map(hex, dense)
    return ''.join(k[2:] if len(k[2:]) == 2 else '0'+k[2:] for k in hexes)

hex_to_bin = lambda s: bin(int(s, 16))[2: ]

#soluzione 1
hashes = [knot_hash(f'stpzcrnm-{i}') for i in range(128)]
bin_hashes = []

for hash in hashes:
    b = ''
    for h in hash:
        temp = hex_to_bin(h)
        b += '0'*(4-len(temp))+temp
    bin_hashes.append(b)

print(sum(row.count('1') for row in bin_hashes))

#soluzione 2
grid = [[int(i) for i in row] for row in bin_hashes]
coordinates = [(x, y) for x, y in product(range(128), repeat=2) if grid[x][y]]

def traverse(x, y):
    coordinates.remove((x, y))
    adjacent = filter(lambda n: n in coordinates, [(x-1, y), (x+1, y), (x, y-1), (x, y+1)])
    for adj in adjacent:
        traverse(*adj)

count = 0
while len(coordinates) > 0:
    traverse(*coordinates[0])
    count += 1

print(count)
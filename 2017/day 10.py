from collections import deque

with open('input10.txt') as file:
    data_raw = file.read()
    data = map(int, data_raw.split(','))

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

#soluzione 1
k = knot_raw(data)
print(k[0]*k[1])

#soluzione 2
print(knot_hash(data_raw))
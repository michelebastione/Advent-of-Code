from itertools import zip_longest


class SuperList(list):
    def __init__(self, item):
        self.item = item

    def __lt__(self, other):
        p1, p2 = self.item, other.item
        if isinstance(p1, int) and isinstance(p2, int):
            if p1 != p2:
                return p1 < p2
        elif isinstance(p1, list) and isinstance(p2, list):
            for z in zip_longest(p1, p2):
                if None in z:
                    return z[0] is None
                else:
                    next_step = SuperList(z[0]) < SuperList(z[1])
                    if next_step is not None:
                        return next_step
        else:
            p1, p2 = map(lambda x: SuperList([x] if isinstance(x, int) else x), [p1, p2])
            return p1 < p2

    def __eq__(self, other):
        return self.item == other.item


with open('input13.txt') as file:
    raw_pairs =[]
    for pair in file.read().strip().split('\n\n'):
        raw_pairs.append(pair.split('\n'))

# solution 1
pairs = [[*map(lambda x: SuperList(eval(x)), pair)] for pair in raw_pairs]
total = 0
for e, pair in enumerate(pairs, 1):
    pair1, pair2 = pair
    if pair1 < pair2:
        total += e
print(total)

# solution 2
divider1, divider2 = map(SuperList, [[[2]], [[6]]])
packets = [divider1, divider2]
for pair in pairs:
    packets.extend([*pair])
packets.sort()
print((packets.index(divider1)+1) * (packets.index(divider2)+1))

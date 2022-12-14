from collections import Counter
from itertools import combinations

with open('input2.txt') as file:
    data = file.read().splitlines()

#soluzione 1
print(sum(1 for box in data if 2 in Counter(box).values()) * sum(1 for box in data if 3 in Counter(box).values()))


#soluzione 2 (un po' brutta ma comunque veloce)
for comb_1, comb_2 in combinations(data, 2):
    s = ''.join([comb_1[char] for char in range(26) if comb_1[char] == comb_2[char]])
    if len(s) == 25:
        print(s)
        break
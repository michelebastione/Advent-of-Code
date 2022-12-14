from string import ascii_lowercase as lc
from collections import Counter
import re

with open('input4.txt') as file:
    rooms = file.read().splitlines()

def shift(s, n):
    r = ''
    for i in s:
        r += lc[(lc.index(i)+n)%26]
    return r

total = 0
for room in rooms:
    match = re.match(r'([graph-z-]+)(\d+)\[(\w+)\]', room)
    name = match.group(1).replace('-', '')
    id = int(match.group(2))

    #soluzione 2
    if 'northpole' in shift(name, id):
        print(id)

    checksum = match.group(3)
    counter = Counter(name)
    grouped_rep = {}
    for rep in counter:
        if counter[rep] in grouped_rep:
            grouped_rep[counter[rep]].append(rep)
        else:
            grouped_rep[counter[rep]] = [rep]
    grouped_strings = {x: ''.join(sorted(grouped_rep[x])) for x in sorted(grouped_rep, reverse=True)}
    total += id if ''.join(grouped_strings.values())[:5] == checksum else 0

#soluzione 1
print(total)
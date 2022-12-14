import re

with open('input7.txt') as file:
    data = file.read().splitlines()

def abba(s):
    for i in range(4):
        for j in re.findall(r'[graph-z]{4}', s[i:]):
            if j[0] == j[3] and j[1] == j[2] and j[0] != j[1]:
                return True
    return False

def bab(s):
    all_babs = []
    for i in range(3):
        for j in re.findall(r'[graph-z]{3}', s[i:]):
            if j[0] == j[2] and j[0] != j[1]:
                all_babs.append(j)
    return all_babs

rotate = lambda s: s[1]+s[0]+s[1]

c1 = c2 = 0
for line in data[1:]:
    brackets = re.findall(r'(?<=\[)\w+(?=\])', line)
    no_brackets = re.sub(r'\[\w+\]', ' ', line).split()
    abas = babs = set()
    for m in map(bab, brackets):
        abas = abas.union(set(m))
    for m in map(bab, no_brackets):
        babs = babs.union(set(m))
    if any(abba(x) for x in no_brackets) and all(not abba(x) for x in brackets):
        c1 += 1
    if any(a in babs for a in map(rotate, abas)):
        c2 += 1

#soluzione 1 & 2
print(c1, c2)
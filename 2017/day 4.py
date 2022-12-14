from itertools import permutations

with open('input4.txt') as file:
    data = file.read().splitlines()

valid = 0
no_anagram = 0
for i in data:
    s = i.split()
    if len(s) == len(set(s)):
        valid += 1
    partial = 0
    total = set()
    for k in s:
        anagram = {*permutations(k)}
        partial += len(anagram)
        total.update(anagram)
    if len(total) == partial:
        no_anagram += 1

#soluzione 1 & 2
print(valid, no_anagram)
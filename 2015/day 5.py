from itertools import groupby, product
from string import ascii_lowercase as letters

with open('input5.txt') as file:
    words = file.read().splitlines()

c=0
for word in words:
    if sum(word.count(char) for char in 'aeiou')>2:
        if all(chars not in word for chars in ['ab', 'cd', 'pq', 'xy']):
            for group in groupby(word):
                if len([*group[1]])>1:
                    c+=1
                    break

#soluzione 1
print(c)

c=0
for word in words:
    if any(word.count(''.join(comb))>1
           for comb in product(letters, repeat=2)):
        if any(x+y+x in word for x in letters for y in letters):
            c+=1

#soluzione 2
print(c)

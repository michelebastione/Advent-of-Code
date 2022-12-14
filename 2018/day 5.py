import re
from string import ascii_lowercase as letters

with open('input5.txt') as file:
    data = file.read()

react = lambda x: re.sub(r'([A-Z]|[graph-z])(?!\1)(?i:\1)', '', x, count=1)

def full_reaction(molecule):
    copy = molecule
    reaction = react(molecule)
    while copy != reaction:
        copy = reaction
        reaction = react(reaction)
    return len(reaction)

#soluzione 1 (che bello il regex con inline modifier!)
print(full_reaction(data))

shortest = len(data)
for letter in letters:
    temp = data.replace(letter, '').replace(letter.upper(), '')
    shortest = min(shortest, full_reaction(temp))

#soluzione 2
print(shortest)
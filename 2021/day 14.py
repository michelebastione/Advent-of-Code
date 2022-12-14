import re
from collections import Counter

with open('input14.txt') as file:
    template, rules = file.read().split('\n\n')
    insertions = {}

for line in rules.splitlines():
    a, b = re.findall(r'\w+', line)
    insertions[a] = b

def step(string):
    result = string[0]
    for i in range(len(string)-1):
        s = string[i: i+2]
        result += f'{insertions[s]}{s[1]}'
    return result


# soluzione 1
for i in range(10):
    print(template)
    template = step(template)
c = Counter(template).values()
print(max(c)-min(c))

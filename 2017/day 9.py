import re

with open('input9.txt') as file:
    data = file.read()

data1 = re.sub(r'!.', '', data)
data2 = re.sub(r'(<[^>]*>)', '', data1)
print(data)
print(data1)
total = 0
bracket_count = 0
for char in data2:
    if char == '{':
        bracket_count += 1
        total += bracket_count
    if char == '}':
        bracket_count -= 1

#soluzione 1
print(total)

#soluzione 2
print(sum(len(garbage)-2 for garbage in re.findall(r'(<[^>]*>)', data1)))
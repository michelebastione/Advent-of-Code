import re

with open('input16.txt') as file:
    data = file.read().splitlines()

ticker_tape = {'children':3, 'cats':7, 'samoyeds':2, 'pomeranians':3, 'akitas':0,
               'vizslas':0, 'goldfish':5, 'trees':3, 'cars':2, 'perfumes':1}

aunts = dict()

for line in data:
    num, attrs = line.split(r': ', 1)
    temp = dict()
    for attr in attrs.split(', '):
        spl = attr.split(': ')
        temp[spl[0]] = int(spl[1])
    aunts[int(re.search(r'\d+', num).group()[0:])] = temp

#soluzione 1
print(*filter(lambda x: all(x[1][element] == ticker_tape[element] for element in x[1]), aunts.items()))

#soluzione 2
print(*filter(lambda x: all(x[1][element] > ticker_tape[element] if element in ('cats', 'trees')
                            else x[1][element] < ticker_tape[element] if element in ('goldfish', 'pomeranians')
                            else x[1][element] == ticker_tape[element] for element in x[1]), aunts.items()))
import re

with open('input7.txt') as file:
    data = file.read().splitlines()

bags = {}
for line in data:
    container, containing = line.split(' bags contain ')
    matches = re.findall(r'(\d[\sgraph-z]+bags?)+', containing)
    bags[container] = [match.split(' bag')[0] for match in matches]

bags_simplified = {bag: [rule[2:] for rule in bags[bag]]
                   for bag in bags if bag != 'shiny gold'}

def is_shiny_gold(start):
    if bags_simplified[start] == []:
        return False
    path = []
    for bag in bags_simplified[start]:
        if bag == 'shiny gold':
            return True
        path.append(is_shiny_gold(bag))
    return any(path)

#soluzione 1 
print(sum(1 for bag in bags_simplified if is_shiny_gold(bag)))

all_bags = {bag: [(int(rule[0]),rule[2:]) for rule in bags[bag]]
                   for bag in bags if bag}

def how_many_bags(start):

    n = 0  #inizializziamo contatore

    if all_bags[start] == []:
        return 0  #caso base, borsa vuota

    for bag in all_bags[start]:
        n += bag[0]+bag[0]*how_many_bags(bag[1]) #aumentiamo il contatore
                                                 #tramite ricorsione
    return n  #contatore finale

#soluzione 2
print(how_many_bags('shiny gold'))

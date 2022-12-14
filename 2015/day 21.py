import re
from itertools import combinations, product

raw_weapons = """Dagger        8     4
Shortsword   10     5
Warhammer    25     6
Longsword    40     7
Greataxe     74     8""".splitlines()

raw_armor = """Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5""".splitlines()

raw_rings = """Damage1    25     1       0
Damage2    50     2       0
Damage3   100     3       0
Defense1   20     0       1
Defense2   40     0       2
Defense3   80     0       3""".splitlines()


weapons = {re.match(r'\w+', line).group():
               dict(zip(['cost', 'damage', 'armor'],
                        [int(i) for i in re.findall(r'\d+', line)]+[0])) for line in raw_weapons}
armor = {re.match(r'\w+', line).group():
             dict(zip(['cost', 'damage', 'armor'],
                      [int(i) for i in re.findall(r'\d+', line)])) for line in raw_armor}
rings = {re.match(r'\w+', line).group():
             dict(zip(['cost', 'damage', 'armor'],
                      [int(i) for i in re.findall(r'\s\d+', line)])) for line in raw_rings}

def win(armor1, damage1):
    attack1 = damage1-2 if damage1-2 > 0 else 1
    attack2 = 8-armor1 if 8-armor1 > 0 else 1
    return 109//attack1 <= 100//attack2

minimum_cost = 10**6
maximum_cost = 0

for i in range(2):
    for j in range(3):
        for prod in product(weapons.values(), combinations(armor.values(), i), combinations(rings.values(), j)):
            defense = attack = cost = 0
            for p in prod:
                if type(p) == dict:
                    defense += p['armor']
                    attack += p['damage']
                    cost += p['cost']
                else:
                    try:
                        defense += sum(x['armor'] for x in p)
                        attack += sum(x['damage'] for x in p)
                        cost += sum(x['cost'] for x in p)
                    except:
                        pass
            if win(defense, attack):
                minimum_cost = min(minimum_cost, cost)
            else:
                maximum_cost = max(maximum_cost, cost)

# Soluzioni 1 & 2
print(minimum_cost, maximum_cost)
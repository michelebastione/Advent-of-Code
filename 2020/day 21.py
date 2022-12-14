with open('input21.txt') as file:
    data = file.read().splitlines()

foods = {}
for line in data:
    ingredients, allergens = line.split(' (contains ')
    foods[tuple(ingredients.split())] = {allergen.strip(')') for allergen in allergens.split(', ')}

ingredients = set()
for ingredient in foods:
    ingredients.update(ingredient)

allergens = set()
for food in foods.values():
    allergens.update({*food})

toxic = set()
for allergen in allergens:
    temp = {*ingredients}
    for food in foods:
        if allergen in foods[food]:
            temp &= set(food)
    toxic |= temp

#soluzione 1
print(sum(len(set(i) - toxic) for i in foods))

possible_combinations = {a: {*toxic} for a in allergens}
for i in possible_combinations:
    for j in foods:
        if i in foods[j]:
            possible_combinations[i] &= set(j)

combinations = {}
while len(possible_combinations) > 0:
    for i in possible_combinations:
        if len(possible_combinations[i]) == 1:
            combinations[i] = possible_combinations[i].pop()
        else:
            for j in combinations.values():
                possible_combinations[i] -= {j}
    possible_combinations = {i: j for i, j in possible_combinations.items() if len(j) > 0}

#soluzione 2
print(','.join(combinations[k] for k in sorted(allergens)))
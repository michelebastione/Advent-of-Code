import numpy as np

recipes = 290431
recipes_score = str(recipes)

scores = '37'
current = [0, 1]

check = True
while True:
    dim = len(scores)
    current = [*map(lambda x: (x+(int(scores[x])+1)) % dim, current)]
    scores += str(sum(map(lambda x: int(scores[x]), current)))
    if check and dim > recipes+10:
        #soluzione 1
        print(scores[recipes: recipes+10])
        check = False
    if dim > 10 and recipes_score in scores[-10:]:
        break

#soluzione 2
print(scores.index(recipes_score))


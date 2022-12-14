from itertools import combinations

discs = [(13, 2), (19, 12), (3, 2), (7, 5), (5, 3), (17, 11)]
discs_adjusted = {i[0]: i[0]-i[1] for i in discs}

def prod(it):
    result = 1
    for i in it:
        result *= i
    return result

def tcr(remainders):
    N = prod(remainders)
    Ni = [prod(combination) for combination in combinations(remainders, len(remainders) - 1)][::-1]
    yi = []
    for i in range(len(Ni)):
        c = 0
        while (Ni[i] * c) % list(remainders)[i] != 1:
            c += 1
        yi.append(c)
    return sum(prod(j) for j in zip(remainders.values(), Ni, yi)) % N

#soluzione 1
print(tcr(discs_adjusted))

#soluzione 2 (nuovo disco dopo gli altri con 11 posizioni e parte da 0)
print(tcr({**discs_adjusted, 11: 4}))


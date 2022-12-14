from collections import Counter

def passwords(r, only_two=False):
    total = 0
    for i in r:
        s = str(i)
        if len(s) != len(set(s)):
            if [*s] == sorted(s):
                if only_two:
                    if any(j == 2 for j in Counter(s).values()):
                        total += 1
                else:
                    total += 1
    return total

#soluzione 1
print(passwords(range(278384, 824795)))

#soluzione 2
print(passwords(range(278384, 824795), True))
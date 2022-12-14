from itertools import permutations

with open('input2.txt') as file:
   matrix = [[int(j) for j in i.split('\t')] for i in file.read().splitlines()]

#soluzione 1
print(sum(max(line)-min(line) for line in matrix))

#soluzione 2
s=0
for line in matrix:
    for p in permutations(line, 2):
        if p[0]%p[1]==0:
            s+=p[0]//p[1]
print(s)


from itertools import combinations

with open('input9.txt') as file:
    data = [int(line) for line in file.read().splitlines()]

check = data[25]
pointer = 0

while check in [sum(combination) for combination in
                combinations(data[pointer:pointer+25],2)]:
    pointer+=1
    check=data[pointer+25]

#soluzione 1
print(check)

for i in range(2, 575):
    for j in range(i):
        if sum(data[j:i])==check:
            #soluzione 2
            print(min(data[j:i])+max(data[j:i]))
            break



with open('input1.txt') as file:
    fix = [*map(int, file.read().splitlines())]

#soluzione 1
print(sum(1 for i in range(1, len(fix)) if fix[i]>fix[i-1]))

#soluzione 2
print(sum(1 for j in range(1, len(fix)) if sum(fix[j:j+3])>sum(fix[j-1:j+2])))
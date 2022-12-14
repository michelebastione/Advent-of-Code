with open('input7.txt') as file:
    positions = [*map(int, file.read().split(','))]

# soluzione 1 & 2
print(min(sum(abs(i-j) for j in positions) for i in range(1000)))
print(min(sum(abs(i-j)*(abs(i-j)+1)//2 for j in positions) for i in range(1000)))
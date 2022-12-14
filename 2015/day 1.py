with open('input1.txt') as file:
    data = file.read()

print(data.count('(') - data.count(')'))

c = 0
for i in range(len(data)):
    c += 1 if data[i] == '(' else -1
    if c < 0:
        print(i+1)
        break

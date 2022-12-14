from collections import Counter

with open('input6.txt') as file:
    data = file.read().splitlines()

message_likely = ''
message_unlikely = ''
for i in range(8):
    counter = Counter([line[i] for line in data]).most_common()
    message_likely += counter[0][0]
    message_unlikely += counter[-1][0]

#soluzioni 1 & 2
print(message_likely, message_unlikely)

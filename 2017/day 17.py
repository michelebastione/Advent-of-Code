buffer = [0]
current = 0

#soluzione 1
for i in range(1, 2018):
    current = (current + 314) % len(buffer)+1
    buffer.insert(current, i)

print(buffer[current+1])

#soluzione 2
zero_index = buffer.index(0)
count = 2018

while count < 5e7:
    current = (current + 314) % count+1
    if current == zero_index:
        zero_index += 1
    elif current == zero_index+1:
        zero_value = count
    count += 1

print(zero_value)
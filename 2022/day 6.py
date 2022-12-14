with open('input6.txt') as file:
    stream = file.read()


def detect_start(n):
    i = 0
    while len(stream[i: i+n]) != len(set(stream[i: i+n])):
        i += 1
    return i+n


# solution 1
print(detect_start(4))

# solution 2
print(detect_start(14))

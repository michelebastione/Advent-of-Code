with open('input20.txt') as file:
    coordinates = [int(line) for line in file]


def mix(numbers, cycles=1):
    size = len(numbers)
    order = [[j, i] for i, j in enumerate(numbers)]
    for _ in range(cycles):
        for num in order:
            val, pos = num
            new_pos = (pos + val) % (size - 1)
            num[1] = new_pos
            for oth in order:
                if oth is not num:
                    if pos < oth[1] <= new_pos:
                        oth[1] = (oth[1] - 1) % size
                    elif new_pos <= oth[1] < pos:
                        oth[1] = (oth[1] + 1) % size

    new_nums = [i[0] for i in sorted(order, key=lambda x: x[1])]
    zero = new_nums.index(0)
    grove = map(lambda x: new_nums[(zero + x) % size], [1000, 2000, 3000])
    return sum(grove)


# solution 1
print(mix(coordinates))

# solution 2 does not work yet :'(
decryption_key = 811589153
new_coordinates = [*map(lambda x: x * decryption_key, coordinates)]
print(mix(new_coordinates, 10))

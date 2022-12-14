import numpy as np

serial_number = 7803
hundreds_digit = lambda x: (x%1000)//100
power_level = lambda x, y: hundreds_digit(((x+10)*y + serial_number) * (x+10))-5

grid = np.array([[power_level(i, j) for j in range(301)] for i in range(301)])

def grid_power(size):
    maximum_power = 0
    maximum_coordinates = (1, 1)
    for i in range(1, 301-size+1):
        for j in range(1, 301-size+1):
            total_power = np.sum(grid[i: i+size, j: j+size])
            if total_power > maximum_power:
                maximum_power = total_power
                maximum_coordinates = (i, j)
    return maximum_power, maximum_coordinates

#soluzione 1
print(grid_power(3)[1])

#soluzione 2 (poco efficiente, da rivedere)
final_size = 1
final_power = 0
final_coordinates = (1, 1)

for i in range(1,301):
    temp = grid_power(i)
    if temp[0] > final_power:
        final_power = temp[0]
        final_coordinates = temp[1]
        final_size = i

print(final_coordinates, final_size)
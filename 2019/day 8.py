import numpy as np

with open('input8.txt') as file:
    data = file.read()
    layers = [[*map(int, data[i: i+25*6])] for i in range(0, len(data), 25*6)]

fewest_zeros = min(layers, key=lambda x: x.count(0))

#soluzione 1
print(fewest_zeros.count(1)*fewest_zeros.count(2))

unlayered = []
for i in range(150):
    for layer in layers:
        if layer[i] == 2:
            continue
        unlayered.append(layer[i])
        break

decoded = np.array(unlayered).reshape((6, 25))
message = np.array([['.']*25]*6)
message[decoded == 1] = '#'

#soluzione 2
for k in range(0, 25, 5):
    print(message[:, k:k+4])
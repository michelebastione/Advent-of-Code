import re
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

with open('input10.txt') as file:
    data = file.read().splitlines()

points_x = np.array([])
velocities_x = np.array([])
points_y = np.array([])
velocities_y = np.array([])

for line in data:
    values = [*map(int, re.findall(r'-?\d+', line))]
    points_x = np.append(points_x, values[0])
    velocities_x = np.append(velocities_x, values[2])
    points_y = np.append(points_y, values[1])
    velocities_y = np.append(velocities_y, values[3])

fig = plt.figure()
axes = plt.axes(xlim=(180, 260), ylim=(160, 240))
points, = axes.plot([], [], 'bo')

def init():
    points.set_data([], [])
    return points

def animate(i):
    x = points_x + velocities_x*i
    y = points_y + velocities_y*i
    points.set_data(x, y)

points_x += velocities_x*10700
points_y += velocities_y*10700

#Nota: la soluzione 1 giunge dopo un po' di trial & error per trovare il riquadro e il frame esatto in cui la scritta appare;
#la soluzione 2 ne consegue dato che è esattamente il numero di frame che cercavamo (-1 perché matplotlib non mostra quello iniziale)
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=11, interval=300, repeat=False)
plt.gca().invert_yaxis()
plt.show()

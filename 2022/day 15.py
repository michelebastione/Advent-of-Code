import re
import numpy as np

with open('input15.txt') as file:
    sep_coords = [*map(int, re.findall(r'-?\d+', prova))]
    sensors = [(i, j) for i, j in zip(sep_coords[::4], sep_coords[1::4])]
    closest_beacons = [(i, j) for i, j in zip(sep_coords[2::4], sep_coords[3::4])]


def distance(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


# all_objects = [*sensors, *closest_beacons]
relative_beacons = dict(zip(sensors, closest_beacons))
distances = {sensor: distance(sensor, beacon) for sensor, beacon in relative_beacons.items()}
min_x, min_y = map(min, [sep_coords[::2], sep_coords[1::2]])
max_x, max_y = map(max, [sep_coords[::2], sep_coords[1::2]])

# solution 1
not_beacons = -1
max_distance = max(distances.values())
for x in range(min_x-max_distance, max_x+max_distance+1):
    point = (x, 2000000)
    not_beacons += any(distance(point, sensor) <= distances[sensor] for sensor in sensors)
print(not_beacons)

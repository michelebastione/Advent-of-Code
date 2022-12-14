import numpy as np
from _collections import deque

cups1 = np.array([int(i) for i in '643719258'])
cups2 = deque([*cups1]+[*range(10, 10**6+1)])

def play(cups, rounds):
    current = cups[0]
    current_index = 0
    round = 0
    length = len(cups)
    while round < rounds:
        if current_index+4 > length:
            cups = np.append(cups, cups[:3])
            cups = np.delete(cups, range(3))
            current_index = np.where(cups == current)[0][0]
        pick_range = range(current_index+1, current_index+4)
        pick = cups[pick_range]
        cups = np.delete(cups, pick_range)
        destination = current-1
        while destination in pick:
            destination -= 1
        if destination < min(cups):
            destination = max(cups)
        destination_index = (np.where(cups == destination)[0][0]+1) % (length-3)
        cups = np.insert(cups, destination_index, pick)
        current_index = (np.where(cups == current)[0][0]+1) % length
        current = cups[current_index]
        round += 1
    return cups

#soluzione 1
print(play(cups1, 100))

def llplay(cups, rounds):
    current = cups2[1]
    current_index = 1
    round = 0
    while round < 10**6:
        break
        round += 1
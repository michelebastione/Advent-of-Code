from collections import deque
import re

with open('input22.txt') as file:
    data = file.read().splitlines()

def deal(deck, increment):
    lg = len(deck)
    new_deck = [0]*lg
    pointer = 0
    while len(deck) > 0:
        new_deck[pointer] = deck.popleft()
        pointer = (pointer + increment) % lg
    return deque(new_deck)

cards = deque(range(10007))
for instr in data:
    if 'stack' in instr:
        cards.reverse()
    else:
        value = int(instr.split()[-1])
        if 'cut' in instr:
            cards.rotate(-value)
        else:
            cards = deal(cards, value)

#soluzione 1
print(cards.index(2019))

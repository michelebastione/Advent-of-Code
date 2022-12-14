from string import ascii_uppercase as letters

with open('input7.txt') as file:
    data = file.read().splitlines()

relations = {letter: [] for letter in letters}
for line in data:
    spl = line.split()
    relations[spl[1]].append(spl[7])

ready1 = [*filter(lambda x: x not in {line.split()[7] for line in data}, letters)]; ready1.sort()
ready2 = [*ready1]
order = ''

while len(order) < 26:
    order += ready1.pop(0)
    possibly_ready = {j for i in order for j in relations[i] if j not in order}
    for p in possibly_ready:
        to_complete_before = {r for r in relations if p in relations[r]}
        if all(k in order for k in to_complete_before):
            if p not in ready1:
                ready1.append(p)
    ready1.sort()

#soluzione 1
print(order)

class Worker():
    def __init__(self):
        self.letter = None
        self.time = 0

    def countdown(self):
        self.time = 61 + letters.index(self.letter)

workers = [Worker() for _ in range(5)]
t = 0
final = ''

while len(final) < 26:
    for worker in workers:
        if worker.letter:
            worker.time -= 1
            if worker.time == 0:
                final += worker.letter
                worker.letter = None

    almost_ready = {j for i in final for j in relations[i] if j not in final}
    for a in almost_ready:
        to_complete = {r for r in relations if a in relations[r]}
        if all(k in final for k in to_complete):
            if a not in ready2 and all(a != w.letter for w in workers):
                ready2.append(a)
    ready2.sort()

    for worker in workers:
        if not worker.letter:
            if len(ready2) > 0:
                worker.letter = ready2.pop(0)
                worker.countdown()

    t += 1 if len(final) < 26 else 0

#soluzione 2
print(t)
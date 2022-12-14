import re

with open('input12.txt') as file:
    raw_data = file.read().splitlines()

data = [re.findall(r'\d+', line) for line in raw_data]
pipes = {int(i[0]): [*map(int, i[1:])] for i in data}

groups = []
def traverse(root):
    groups[-1].append(root)
    for pipe in pipes[root]:
        if pipe not in groups[-1]:
            traverse(pipe)
    del[pipes[root]]

while len(pipes) > 0:
    groups.append(list())
    traverse([*pipes.keys()][0])

#soluzione 1
print(len(groups[0]))

#soluzione 2
print(len(groups))


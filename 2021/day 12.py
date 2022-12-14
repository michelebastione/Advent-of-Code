with open('input12.txt') as file:
    paths = {}
    for line in file:
        a, b = line.split('-')
        b = b.strip()
        if a in paths:
            paths[a].append(b)
        else:
            paths[a] = [b]
        if b in paths:
            paths[b].append(a)
        else:
            paths[b] = [a]

for path in paths:
    if 'start' in paths[path]:
        paths[path].remove('start')

# soluzione 1
count = 0

def traverse(start, traversed=[]):
    global count
    if start.islower():
        traversed.append(start)
    for node in paths[start]:
        if node == 'end':
            count += 1
        elif node not in traversed:
            traverse(node, [*traversed])

traverse('start')
print(count)

# soluzione 2
count_again = 0
lower_case_nodes = {i: 0 for i in paths if i.islower()}
del lower_case_nodes['start']
del lower_case_nodes['end']

def traverse_again(start, traversed=lower_case_nodes):
    global count_again
    if start.islower() and start != 'start':
        traversed[start] += 1
    for node in paths[start]:
        if node == 'end':
            count_again += 1
        elif node.isupper() or traversed[node]==0:
            traverse_again(node, {**traversed})
        elif traversed[node]==1 and all(k<2 for k in traversed.values()):
            traverse_again(node, {**traversed})

traverse_again('start')
print(count_again)

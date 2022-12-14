
with open('input6.txt') as file:
    groups_raw = file.read().split('\n\n')

groups = [{answer for answer in group if answer!='\n'} for group in groups_raw]

#soluzione 1
print(sum(len(group) for group in groups))

groups_separate = [group.split('\n') for group in groups_raw]
intersection = []
for group in groups_separate:
    if len(group)==1:
        intersection.append([each for each in group[0]])
        continue
    intersection.append([answer for answer in group[0] if all(answer in each for each in group[1:])])

#soluzione 2
print(sum(len(group) for group in intersection))

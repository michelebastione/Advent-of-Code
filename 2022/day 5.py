import re, copy

with open('input5.txt') as file:
    raw_stacks, raw_instructions = file.read().split('\n\n')

stacks = [[] for _ in range(9)]
for line in raw_stacks.splitlines()[:-1]:
    elements = {i: line[1+i*4] for i in range(9)}
    for stack, element in elements.items():
        if element != ' ':
            stacks[stack].insert(0, element)
instructions = [[*map(int, re.findall(r'\d+', line))] for line in raw_instructions.splitlines()]

# solution 1
stacks_1 = copy.deepcopy(stacks)
for n, s1, s2 in instructions:
    for _ in range(n):
        crate = stacks_1[s1-1].pop()
        stacks_1[s2-1].append(crate)
print(''.join(stack[-1] for stack in stacks_1))

# solution 2
stacks_2 = copy.deepcopy(stacks)
for n, s1, s2 in instructions:
    temp_stack = []
    for _ in range(n):
        crate = stacks_2[s1-1].pop()
        temp_stack.insert(0, crate)
    stacks_2[s2-1].extend(temp_stack)
print(''.join(stack[-1] for stack in stacks_2))

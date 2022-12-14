current_state = [int(i) for i in "4	10	4	1	8	4	9	14	5	1	14	15	0	15	3	5".split()]
states = []

def reallocate(array):
    copy = [*array]
    to_redistr = max(copy)
    ind = array.index(to_redistr)
    copy[ind] = 0
    while to_redistr > 0:
        ind = (ind+1) % len(copy)
        copy[ind] += 1
        to_redistr -= 1
    return copy

count = 0
while current_state not in states:
    states.append(current_state)
    current_state = reallocate(current_state)
    count += 1

#soluzioni 1 & 2
print(count, count - states.index(current_state))
with open('input6.txt') as file:
    data = [*map(int, file.read().split(','))]
fish = {i: data.count(i) for i in range(9)}


def tick(timer, days):
    for _ in range(days):
        new_timer = {k: timer[k+1] for k in range(6)}
        new_timer[6], new_timer[7], new_timer[8] = timer[0]+timer[7], timer[8], timer[0]
        timer = new_timer
    return timer


# soluzione 1 & 2
print(sum(tick(fish, 80).values()))
print(sum(tick(fish, 256).values()))

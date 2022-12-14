import re

with open('input14.txt') as file:
    raw = file.read().splitlines()
    data = {x.split()[0]: [int(i) for i in re.findall(r'\d+', x)] for x in raw}

seconds = 2503
def distance(speed, pace, rest, time):
    cycles, reminder = divmod(time, pace+rest)
    if reminder < pace:
        return speed*cycles*pace + reminder*speed
    return speed*(cycles+1)*pace

#Soluzione 1
print(max(distance(*value, seconds) for value in data.values()))

def scoring(reinders, time):
    results  = {reinder: 0 for reinder in reinders}
    for i in range(1, time+1):
        subtotal = {reinder: distance(*reinders[reinder], i) for reinder in reinders}
        for reinder in results:
            results[reinder] += 1 if subtotal[reinder] == max(subtotal.values()) else 0
    return max(results.values())

#Soluzione 2
print(scoring(data, seconds))
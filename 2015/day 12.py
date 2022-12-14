import json, re

with open('input12.txt') as file:
    raw_input = file.read()

    #solzuione 1
    print(sum(int(n) for n in re.findall(r'-?\d+', raw_input)))

    data = json.loads(raw_input)

def recursive_counting(object):

    def scan(subtotal, iterable):
        for element in iterable:
            if type(element) in [dict, list]:
                subtotal += recursive_counting(element)
            elif type(element) == int:
                subtotal += element
        return subtotal

    total = 0
    if type(object) == dict:
        if 'red' in object.values():
            return 0
        total += scan(total, object.values())

    if type(object) == list:
        total += scan(total, object)

    return total

#soluzione 2
print(recursive_counting(data))
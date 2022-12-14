with open('input8.txt') as file:
    wires = []
    outputs = []
    for line in file:
        data = line.split(' | ')
        wires.append(data[0].split())
        outputs.append(data[1].split())

# soluzione 1
print(sum(sum(1 for j in i if len(j) in (2, 3, 4, 7)) for i in outputs))

# soluzione 2
def decode(wire):
    lengths = {length: [w for w in wire if len(w) == length] for length in range(2, 8)}
    for length in lengths:
        if length < 5 or length == 7:
            lengths[length] = lengths[length][0]
    final = {}
    final['top'] = {*lengths[3]} - {*lengths[2]}

    for i in lengths[6]:
        temp = {*i} & {*lengths[2]}
        if len(temp) == 1:
            final['botr'] = temp
            final['topr'] = {*lengths[2]} - temp
            break

    for j in lengths[6]:
        temp1 = {*lengths[4]} - final['topr'] - final['botr']
        temp2 = temp1 & {*j}
        if len(temp2) == 1:
            final['topl'] = temp2
            final['cen'] = temp1 - temp2
            break

    for k in lengths[5]:
        temp = {*k} - final['top'] - final['topr'] - final['cen'] - final['botr']
        if len(temp) == 1:
            final['bot'] = temp
            final = {a: list(final[a]).pop() for a in final}
            final['botl'] = list(({*lengths[7]} - set(final.values()))).pop()
            break

    return {value: key for key, value in final.items()}

seven_segments = {
    ('top', 'topr', 'topl', 'botl', 'botr', 'bot'): '0',
    ('topr', 'botr'): '1',
    ('top', 'topr', 'cen', 'botl', 'bot'): '2',
    ('top', 'topr', 'cen', 'botr', 'bot'): '3',
    ('topl', 'topr', 'cen', 'botr'): '4',
    ('top', 'topl', 'cen', 'botr', 'bot'): '5',
    ('top', 'topl', 'cen', 'botl', 'botr', 'bot'): '6',
    ('top', 'topr', 'botr'): '7',
    ('top', 'topr', 'topl', 'cen', 'botl', 'botr', 'bot'): '8',
    ('top', 'topr', 'topl', 'cen', 'botr', 'bot'): '9'
}

total = 0
for wire, output in zip(wires, outputs):
    wiring = decode(wire)
    num = ''
    for out in output:
        segments = {wiring[o] for o in out}
        for key in seven_segments:
            if set(key) == segments:
                num += seven_segments[key]
    total += int(num)

print(total)

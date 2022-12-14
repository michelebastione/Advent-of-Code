import regex

def parse(start, part_2 = False):
    to_compile = ''
    if len(start) == 1:
        return start
    elif type(start) != str:
        for e in start:
            to_compile += parse(e, part_2=part_2)
    elif '|' in start:
        s = start.split('|')
        to_compile += '('+parse(eval(s[0][1:-1]), part_2=part_2)+'|'+parse(eval(s[1][1:-1]), part_2=part_2)+')'
    elif ',' in start:
        s = start.split(',')
        if part_2 and start == 'rules[42],rules[31]':
            to_compile += '(?P<r42>'+parse(eval(s[0]), part_2=part_2) + '(?&r42)?' + parse(eval(s[1]), part_2=part_2)+')'
            return to_compile
        to_compile += parse(eval(s[0]), part_2=part_2)+parse(eval(s[1]), part_2=part_2)
    else:
        to_compile += parse(eval(start), part_2=part_2)
        if part_2 and start == 'rules[42]':
            to_compile += '+'
    return to_compile

with open('input19.txt') as file:
    instructions, data = file.read().split('\n\n')
strings = data.splitlines()
rules = {int(instruction.split(': ')[0]): instruction.split(': ')[1]
         for instruction in instructions.splitlines()}

for rule in rules:
    r = rules[rule]
    if '|' in r:
        rules[rule] = '('+r[:r.index('|')-1]+')|('+r[r.index('|')+2:]+')'
    rules[rule] = rules[rule].replace(' ', ',')
    rules[rule] = regex.sub(r'\d+', r'rules[\g<0>]', rules[rule])

pattern_1 = parse(rules[0])
pattern_2 = parse(rules[0], True)

#soluzione 1
print(sum(1 for line in strings if regex.fullmatch(pattern_1, line)))

#soluzione 2
print(sum(1 for line in strings if regex.fullmatch(pattern_2, line)))

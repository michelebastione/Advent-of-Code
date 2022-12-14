import re

with open('input18.txt') as file:
    data = file.read().splitlines()

for line in range(len(data)):
    data[line] = data[line].replace(' ', '')

def bracket_match(string):
    count = 0
    for i in range(len(string)):
        if string[i] == '(':
            count += 1
        if string[i] == ')':
            if count == 0:
                return i+1
            count -= 1

def solve(expr):
    if expr[0].isdigit():
        partial = int(expr[0])
        pointer = 1
    else:
        finish = bracket_match(expr[1:])
        partial = solve(expr[1:finish])
        pointer = finish+1

    while pointer < len(expr):
        if expr[pointer+1] != '(':
            partial = eval(str(partial)+expr[pointer:pointer+2])
            pointer += 2
        else:
            stop = bracket_match(expr[pointer+2:])
            partial = eval(str(partial)+expr[pointer]+str(solve(expr[pointer+1:pointer+stop+2])))
            pointer += stop+2

    return partial

#soluzione 1
print(sum(solve(expression) for expression in data))

def tokenized_solver(n):
    while '(' in n:
        span_0 = n.index('(')
        span_1 = span_0 + bracket_match(n[span_0 + 1:])
        n = n[:span_0] + tokenized_solver(n[span_0 + 1: span_1]) + n[span_1 + 1:]

    while (match := re.search('\d+\+\d+', n)):
        new = str(eval(match.group(0)))
        span = match.span()
        n = n[:span[0]] + new + n[span[1]:]

    return str(eval(n))

#soluzione 2
print(sum(int(tokenized_solver(expression)) for expression in data))
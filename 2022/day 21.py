import re

with open('input21.txt') as file:
    instructions = {}
    for line in file:
        i, j = line.split(": ")
        instructions[i] = j.strip()


def execute(monkeys):
    results = {}
    while 'root' not in results:
        for monkey, instruction in monkeys.items():
            if monkey in results:
                continue
            if instruction.isdigit():
                results[monkey] = int(instruction)
            else:
                a, b = re.findall(r"\w+", instruction)
                op = re.search(r"[+*-/]", instruction).group()
                if a in results and b in results:
                    results[monkey] = eval(f"results[\"{a}\"] {op} results[\"{b}\"]")
    return results['root']


# solution 1
print(int(execute(instructions)))

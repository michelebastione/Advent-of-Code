from copy import deepcopy

with open('input11.txt') as file:
    config = {}
    multiplier = 1
    for n, monkey in enumerate(file.read().split("\n\n")):
        data = monkey.splitlines()
        items, operation, test, true, false = [*map(lambda x: x.split(": ")[1], data[1:])]
        config[n] = {}
        config[n]["items"] = [*map(int, items.split(","))]
        operation = operation.replace("old", "current_item")
        config[n]["operation"] = operation.split("= ")[1]
        config[n]["test"] = int(test.split()[-1])
        multiplier *= config[n]["test"]
        config[n][True] = int(true.split()[-1])
        config[n][False] = int(false.split()[-1])
        config[n]["inspected"] = 0


def monkey_business(rounds, relief=True):
    monkeys = deepcopy(config)
    for _ in range(rounds):
        for monkey in monkeys.values():
            monkey["inspected"] += len(monkey["items"])
            while monkey["items"]:
                current_item = monkey["items"].pop(0)
                new_level = eval(monkey["operation"])
                if relief:
                    new_level //= 3
                new_level %= multiplier
                result = new_level % monkey["test"] == 0
                next_monkey = monkey[result]
                monkeys[next_monkey]["items"].append(new_level)
    most_active = sorted([monkey["inspected"] for monkey in monkeys.values()], reverse=True)
    return most_active[0]*most_active[1]


# solution 1
print(monkey_business(20))

# solution 2
print(monkey_business(10000, False))

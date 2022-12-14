with open("input1.txt") as file:
    raw_calories = file.read().strip().split("\n\n")
    calories = [[*map(int, elf.split("\n"))] for elf in raw_calories]
    total_calories = [sum(elf) for elf in calories]

# solution 1
print(max(total_calories))

#solution 2
print(sum(sorted(total_calories, reverse=True)[:3]))

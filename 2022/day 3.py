from string import ascii_letters
priorities = {let: num for num, let in enumerate(ascii_letters, 1)}

with open('input3.txt') as file:
    rucksacks = file.read().splitlines()

# solution 1
compartments = [({*sack[:len(sack)//2]}, {*sack[len(sack) // 2:]}) for sack in rucksacks]
common_letters = [(comp[0] & comp[1]).pop() for comp in compartments]
print(sum([priorities[letter] for letter in common_letters]))

# solution 2
groups = [rucksacks[i: i+3] for i in range(0, len(rucksacks), 3)]
badges = [(set(group[0]) & set(group[1]) & set(group[2])).pop() for group in groups]
print(sum([priorities[badge] for badge in badges]))

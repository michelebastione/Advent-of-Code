with open("input12.txt") as file:
    data = file.read().splitlines()
    initial_state = 30*"." + data[0].split(": ")[1] + 30*"."
    pots = {line.split(' => ')[0]: line.split(" => ")[1] for line in data[2:]}

length = len(initial_state)-2
for e in range(20):
    current_state = ".."
    for i in range(2, length):
        current_state += pots[initial_state[i-2: i+3]]
    current_state += '..'
    initial_state = current_state

#soluzione 1
print(sum(-i for i in range(31) if current_state[:31][::-1][i] == "#") +
      sum(i for i in range(length-30) if current_state[30:][i] == "#"))
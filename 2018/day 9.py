players = 400
marbles = 718640

config = [0, 1]
scores = dict()
pointer = 1

i = 2
while i <= marbles:
    if i % 23 == 0:
        to_remove = (pointer-7) % len(config)
        pointer = (pointer-7) % len(config)
        current_score = i + config.pop(to_remove)
        if (player := i%players) in scores:
            scores[player] += current_score
        else:
            scores[player] = current_score
    else:
        pointer = (pointer + 2) % len(config)
        config.insert(pointer, i)
    i += 1

#soluzione 1
print(max(scores.values()))
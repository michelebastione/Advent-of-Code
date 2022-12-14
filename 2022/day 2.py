with open('input2.txt') as file:
    rounds = [(line.split()) for line in file.readlines()]

score_1 = 0
score_2 = 0
for r in rounds:
    score_1 += {"X": 1, "Y": 2, "Z": 3}[r[1]]
    score_2 += {"X": 0, "Y": 3, "Z": 6}[r[1]]

    if r in [["A", "Y"], ["B", "Z"], ["C", "X"]]:
        score_1 += 6
    elif r in [["A", "X"], ["B", "Y"], ["C", "Z"]]:
        score_1 += 3

    if r[1] == "X":
        score_2 += {"A": 3, "B": 1, "C": 2}[r[0]]
    elif r[1] == "Y":
        score_2 += {"A": 1, "B": 2, "C": 3}[r[0]]
    else:
        score_2 += {"A": 2, "B": 3, "C": 1}[r[0]]


# solution 1
print(score_1)

# solution 2
print(score_2)

class Stack:
    b1 = '{[(<'
    b2 = '}])>'
    matches_1 = dict(zip(b2, b1))
    matches_2 = dict(zip(b1, b2))
    points_corrupted = dict(zip(b2, [1197, 57, 3, 25137]))
    points_incomplete = dict(zip(b2, [3, 2, 1, 4]))

    def __init__(self, string):
        self.string = string

    def corruption_score(self):
        self.stack = []
        for s in self.string:
            if s in self.b1:
                self.stack.append(s)
            else:
                if self.matches_1[s] != self.stack.pop():
                    self.corrupted = True
                    return self.points_corrupted[s]
        self.corrupted = False
        return 0

    def complete(self):
        total = 0
        for c in self.stack[::-1]:
            total *= 5
            total += self.points_incomplete[self.matches_2[c]]
        return total

with open('input10.txt') as file:
    lines = [Stack(line) for line in file.read().splitlines()]

# soluzione 1
print(sum(line.corruption_score() for line in lines))

# soluzione 2
incomplete = filter(lambda x: not x.corrupted, lines)
all_scores = [line.complete() for line in incomplete]
print(sorted(all_scores)[len(all_scores)//2])
import numpy as np

with open('input4.txt') as file:
    data = file.read().split('\n\n')
    drawn = [*map(int, data[0].split(','))]
    raw_boards = [np.array([[*line.split()] for line in board.splitlines()], dtype=int) for board in data[1:]]


class Board:
    def __init__(self, board):
        self.board = board
        self.marked = []
        self.score = 0
        self.count = 0

    def unmarked_sum(self):
        return self.board.sum() - sum(self.marked)

    def draw(self, n):
        self.count += 1
        if n in self.board:
            self.marked.append(n)
        for line in [row for row in self.board] + [col for col in self.board.transpose()]:
            if self.bingo(line):
                self.score = n*self.unmarked_sum()

    def bingo(self, nums):
        return np.isin(nums, self.marked).all()


# soluzioni 1 & 2
boards = [Board(board) for board in raw_boards]
for num in drawn:
    for board in boards:
        if board.score == 0:
            board.draw(num)

print(min(boards, key=lambda x: x.count).score)
print(max(boards, key=lambda x: x.count).score)

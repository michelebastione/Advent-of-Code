import numpy as np
from copy import copy

with open('input18.txt') as file:
    data = np.array([[i for i in line] for line in file.read().splitlines()])

data1 = copy(data)
data1[0,99] = '#'
data1[99,0] = '#'

class Automa:
    def __init__(self, cells):
        self.cells = copy(cells)
        self.copy = copy(cells)

    def adjacent(self, x, y):
        c = self.cells
        if x==0 and y==0:
            border = [c[0,1], c[1,0], c[1,1]]
        elif x==y==99:
            border = [c[99,98], c[98,99], c[98,98]]
        elif y==99 and x==0:
            border = [c[0,98], c[1,98], c[1,99]]
        elif y==0 and x==99:
            border = [c[99,1], c[98,0], c[98,1]]
        elif x==0:
            border = list(c[1,y-1:y+2].reshape(3))+[c[x,y-1], c[x,y+1]]
        elif x==99:
            border = list(c[98,y-1:y+2].reshape(3))+[c[x,y-1], c[x,y+1]]
        elif y==99:
            border = list(c[x-1:x+2,98].reshape(3))+[c[x-1,y], c[x+1,y]]
        elif y==0:
            border = list(c[x-1:x+2,1].reshape(3))+[c[x-1,y], c[x+1,y]]
        else:
            border = list(c[x-1:x+2, y-1:y+2].reshape(9))
            del border[4]
        return border

    def solve(self, corners = False):
        for row in range(100):
            for column in range(100):
                if corners:
                    if row in (0,99) and column in (0,99):
                        continue
                adj = self.adjacent(row, column)
                if self.cells[row, column] == '.' and adj.count('#')==3:
                    self.copy[row, column] = '#'
                elif self.cells[row, column] == '#' and adj.count('#') not in (2,3):
                    self.copy[row, column] = '.'
        self.cells = copy(self.copy)

grid = Automa(data)
grid1 = Automa(data1)
for _ in range(100):
    grid.solve()
    grid1.solve(True)

#soluzione 1
print(np.count_nonzero(grid.cells == '#'))

#soluzione 2
print(np.count_nonzero(grid1.cells == '#'))
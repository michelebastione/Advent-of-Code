with open('input8.txt') as file:
    data = [*map(int, file.read().split())]

class Tree:
    def __init__(self, parent=None):
        self.children = []
        self.parent = parent

root = Tree()

current = root
pointer = 0
while pointer < len(data):
    children, meta = data[pointer: pointer+2]
    if children == 0:
        current.metadata = data[pointer+2: pointer+meta+2]
        pointer += meta+2
        current = current.parent
    else:
        current.n_children = children
        current.len_meta = meta
        current.children.append(Tree(current))
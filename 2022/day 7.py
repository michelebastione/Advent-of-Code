with open('input7.txt') as file:
    terminal = file.read().splitlines()


class Tree:
    def __init__(self, parent=None, size=0):
        self.parent = parent
        self.children = []
        self.size = size

    def update_size(self):
        for child in self.children:
            child.update_size()
            self.size += child.size

    def total_sizes_sum(self, cutoff):
        total = self.size if self.size <= cutoff and self.children else 0
        for child in self.children:
            total += child.total_sizes_sum(cutoff)
        return total

    def find_smallest_above(self, cutoff, min_value=7e7):
        for child in self.children:
            if child.children and child.size >= cutoff:
                min_value = min(child.size, child.find_smallest_above(cutoff, min_value))
        return min_value


main_root = Tree()

for line in terminal:
    tokens = line.split()
    if "$" in tokens:
        if "cd" in tokens:
            if "/" in tokens:
                current_path = main_root
            elif ".." in tokens:
                current_path = current_path.parent
            else:
                current_path = current_path.__getattribute__(tokens[-1])
    else:
        child = Tree(current_path, 0 if "dir" in tokens else int(tokens[0]))
        current_path.__setattr__(tokens[1], child)
        current_path.children.append(child)

main_root.update_size()

# solution 1
print(main_root.total_sizes_sum(1e5))

# solution 2
space_needed = 3e7 - (7e7-main_root.size)
print(main_root.find_smallest_above(space_needed))

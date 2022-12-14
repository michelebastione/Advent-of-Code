import re

with open('input7.txt') as file:
    data = file.read().splitlines()

directories = {}
for directory in data:
    subs = re.findall(r'[graph-z]+', directory)
    weight = int(re.search(r'\d+', directory).group())
    directories[subs[0]] = (weight, subs[1:])

#soluzione 1
for d1 in directories:
    if all(d1 not in directories[d2][1] for d2 in directories):
        main_root = d1
        print(main_root)
        break

class Tree:
    def __init__(self, root):
        self.root = root
        self.weight = directories[root][0]
        self.children = [Tree(child) for child in directories[root][1]]

    def tree_sum(self):
        return self.weight + sum(child.tree_sum() for child in self.children)

    def wrong_sum(self):
        children_sums = {child: child.tree_sum() for child in self.children}
        M, m = max(children_sums.values()), min(children_sums.values())
        difference = M-m if [*children_sums.values()].count(M) == 1 else m-M
        for s in children_sums:
            if [*children_sums.values()].count(children_sums[s]) == 1:
                if len(set(t.tree_sum() for t in s.children)) == 1:
                    return s.weight - difference
                return s.wrong_sum()

#soluzione 2
print(Tree(main_root).wrong_sum())

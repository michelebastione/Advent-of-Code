with open('input6.txt') as file:
    data = file.read().splitlines()
    orbits = dict()
    for i in data:
        o1, o2 = i.split(')')
        if o1 in orbits:
            orbits[o1].append(o2)
        else:
            orbits[o1] = [o2]

class Tree():
    def __init__(self, root, current_orbit=0):
        self.root = root
        self.children = []
        self.current_orbit = current_orbit
        if root in orbits:
            for child in orbits[root]:
                self.children.append(Tree(child, current_orbit+1))

    def checksum_orbits(self):
        return self.current_orbit + sum(child.checksum_orbits() for child in self.children)

    # def find_child(self, name):
    #     if self.root == name:
    #         return self
    #     for child in self.children:
    #         final = child.find_child(name)
    #         if final != None:
    #             return final

    def find_route(self, object, route=[]):
        if object == self.root:
            return route + [self.root]
        for child in self.children:
            final = child.find_route(object, route+[self.root])
            if final != None:
                return final

main_root = Tree('COM')

#soluzione 1
print(main_root.checksum_orbits())

def distance(root, t1, t2):
    r1, r2 = root.find_route(t1), root.find_route(t2)
    #r1, r2 = min(r1, r2), max(r1, r2)
    c = 0
    while r1[c] == r2[c]:
        c += 1
    return len(r1[c:]) + len(r2[c:]) - 2

#soluzione 2
print(distance(main_root, 'YOU', 'SAN'))
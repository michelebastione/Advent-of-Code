from copy import deepcopy

with open('input13.txt') as file:
    data = file.read().splitlines()

layers = {}
for line in data:
    spl = line.split(': ')
    layers[int(spl[0])] = int(spl[1])

class Scanner:
    def __init__(self, layers):
        self.layers = layers
        self.scanning = {layer: [0, 1] for layer in layers}

    def clock_scanners(self, scanners):
        for scanner in scanners:
            if scanners[scanner][1]:
                if scanners[scanner][0] == self.layers[scanner]-1:
                    scanners[scanner][1] = 0
                    scanners[scanner][0] -= 1
                else:
                    scanners[scanner][0] += 1
            else:
                if scanners[scanner][0] == 0:
                    scanners[scanner][1] = 1
                    scanners[scanner][0] = 1
                else:
                    scanners[scanner][0] -= 1

    def severity(self, scanner):
        total = 0
        for i in range(max(self.layers)+1):
            if i in self.layers:
                if scanner[i][0] == 0:
                    total += i*self.layers[i]
            self.clock_scanners(scanner)
        return total

    def simple_collision(self, scanner):
        for i in range(max(self.layers)+1):
            if i in self.layers:
                if scanner[i][0] == 0:
                    return True
            self.clock_scanners(scanner)
        return False

    def not_caught(self):
        delay = 0
        temp = deepcopy(self.scanning)
        while self.simple_collision(temp):
            self.clock_scanners(self.scanning)
            temp = deepcopy(self.scanning)
            delay += 1
        return delay

#soluzione 1
S1 = Scanner(layers)
print(S1.severity(S1.scanning))

#soluzione 2 (estremamente non ottimizzata, termina in 10 minuti)
S2 = Scanner(layers)
print(S2.not_caught())
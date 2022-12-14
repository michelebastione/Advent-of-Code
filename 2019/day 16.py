from itertools import cycle

with open('input16.txt') as file:
    signal = file.read()

def pattern(l):
    for i in range(l-1):
        yield 0
    yield from cycle([1]*l+[0]*l+[-1]*l+[0]*l)

def fft(s):
    new = ''
    for i in range(len(s)):
        p = pattern(i+1)
        tot = sum(int(j)*next(p) for j in s)
        new += str(tot)[-1]
    return new

for i in range(100):
    signal = fft(signal)

#soluzione 1
print(signal[:8])
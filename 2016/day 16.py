def dragon_curve(s, n):
    while len(s) < n:
        s = s + '0' + ''.join('1' if i == '0' else '0' for i in s[::-1])
    return s[:n]

def checksum(cs):
    while True:
        temp = [cs[i: i+2] for i in range(0, len(cs), 2)]
        cs = ''.join('1' if j == j[::-1] else '0' for j in temp)
        if len(cs)%2 == 1:
            return cs

#soluzione 1
print(checksum(dragon_curve('11011110011011101', 272)))

#soluzione 2 (impiega una manciata di secondi, ma c'è sicuramente un trucco per velocizzarlo)
print(checksum(dragon_curve('11011110011011101', 35651584)))
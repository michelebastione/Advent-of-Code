a, b = 722, 354
values = count = 0

while count < 4e7:
    a = (a*16807) % 2147483647
    b = (b*48271) % 2147483647
    ba, bb = bin(a)[2:], bin(b)[2:]
    ba, bb = '0'*(16-len(ba))+ba, '0'*(16-len(bb))+bb
    values += ba[-16:] == bb[-16:]
    count += 1

#soluzione 1
print(values)

a, b = 722, 354
values = count = 0

while count < 5e6:
    a = (a*16807) % 2147483647
    while a%4 != 0:
        a = (a * 16807) % 2147483647
    b = (b*48271) % 2147483647
    while b%8 != 0:
        b = (b * 48271) % 2147483647
    ba, bb = bin(a)[2:], bin(b)[2:]
    ba, bb = '0'*(16-len(ba))+ba, '0'*(16-len(bb))+bb
    values += ba[-16:] == bb[-16:]
    count += 1

#soluzione 2 (sono entrambe estremamente inefficienti, da ottimizzare)
print(values)
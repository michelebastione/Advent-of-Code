import re

with open('input9.txt') as file:
    data = file.read()

pattern = re.compile(r'\((\d+)y(\d+)\)')
pattern1 = re.compile(r'(\((\d+)y(\d+)\))+')
pattern2 = re.compile(r'\([^\)]+\)')

ind = 0
decompressed = ''

while ind < len(data):
    temp = re.match(pattern, data[ind:])
    if temp:
        length = len(temp.group(0))
        substring = int(temp.group(1))
        repetition = int(temp.group(2))
        decompressed += data[ind+length : ind+length+substring] * repetition
        ind += length+substring
    else:
        pass
        decompressed += data[ind]
        ind += 1

#soluzione 1
print(len(decompressed))

def recursive_decompression(string):
    ind = 0
    total = 0
    while ind < len(string):
        match = re.match(pattern, string[ind:])
        if match:
            start = ind + len(match.group(0))
            substring = string[start : start + int(match.group(1))]
            repetition = int(match.group(2))
            total += recursive_decompression(substring) * repetition
            ind = start + len(substring)
        else:
            total += 1
            ind += 1
    return total

# soluzione 2 (nota: si potrebbero unire i 2 passaggi in una sola funzione)
print(recursive_decompression(data))
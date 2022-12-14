import re
from itertools import product

with open('input14.txt') as file:
    data = [line.splitlines() for line in file.read().split('mask = ')[1:]]

def mem_write(n=0):
    mem = {}
    for line in data:
        for expr in line[1:]:
            key = re.search(r'\d+',expr).group()
            value = expr.split(' = ')[1]
            line_inv = line[0][::-1]
            value_bin_inv = bin(int(value))[:1:-1]
            key_bin_inv = bin(int(key))[:1:-1]
            sub = ''

            if n==0:
                for char in range(36):
                    if line_inv[char] in '01':
                        sub += line_inv[char]
                    elif char < len(value_bin_inv):
                        sub += value_bin_inv[char]
                    else:
                        sub += '0'
                mem[key] = int(sub[::-1],2)

            else:
                c = line_inv.count('X')
                for char in range(36):
                    if line_inv[char] == '1':
                        sub += '1'
                    elif line_inv[char] == '0':
                        sub += key_bin_inv[char] if char < len(key_bin_inv) else '0'
                    else:
                        sub += '}{'
                sub = sub[::-1]
                for combination in product('01', repeat = c):
                    mem[int(sub.format(*combination),2)] = int(value)
           
    return mem

#soluzione 1        
print(sum(mem_write().values()))

#soluzione 2  
print(sum(mem_write(1).values()))

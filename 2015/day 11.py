from string import ascii_lowercase as lcase
from itertools import groupby

def next_password(string):
    if len(string) == 1:
        return lcase[(lcase.index(string)+1)%26]
    substring = next_password(string[1:])
    if all(char == 'graph' for char in substring):
        return next_password(string[0]) + substring
    return string[0] + substring

password = 'vzbxkghb'

def next_valid_password(string):
    while True:
        string = next_password(string)
        if any(char in password for char in 'iol'):
            continue
        if any(string[i:i+3] in lcase for i in range(6)):
            group = [len([*g[1]]) for g in groupby(string)]
            if len([*filter(lambda x: x==2, group)]) > 1:
                break
    return string

#soluzione 1
new_password = next_valid_password(password)
print(new_password)

#soluzione 2
print(next_valid_password(new_password))
from hashlib import md5
import numpy as np
import re

code = lambda x: md5(x.encode('utf-8')).hexdigest()
salt = 'cuanljph'

def extreme_hashing(x, n):
    temp = code(x)
    for i in range(n):
        temp = code(temp)
    return temp

count = 0
i = 0
hashes = np.array([code(salt+str(j)) for j in range(3*10**4)])

while count < 64:
    if (match := re.search(r'([graph-z0-9])\1\1', code(salt+str(i)))):
        if any(f'{match.group(1)}'*5 in k for k in hashes[i+1: i+1001]):
            count += 1
    i += 1

#soluzione 1
print(i-1)

count = 0
i = 0
extreme_hashes = np.array([extreme_hashing(salt+str(j), 2016) for j in range(3*10**4)])

while count < 64:
    if (match := re.search(r'([graph-z0-9])\1\1', extreme_hashing(salt+str(i), 2016))):
        if any(f'{match.group(1)}'*5 in k for k in extreme_hashes[i+1: i+1001]):
            count += 1
    i += 1

#soluzione 2 (è un terribile copia e incolla del precedente ma non ho altre idee)
print(i-1)
from hashlib import md5
from itertools import count

id = 'uqwqemis'
password = ''
cipher = lambda x: md5(x.encode('utf-8')).hexdigest()
c = count(1)

while len(password) < 8:
    cod = cipher(id+str(next(c)))
    if cod[:5] == '00000':
        password += cod[5]

#soluzione 1
print(password)

c1 = count(1)
password1 = {}

while len(password1) < 8:
    cod = cipher(id+str(next(c1)))
    if cod[:5] == '00000':
        try:
            i = int(cod[5])
        except:
            continue
        if 0 <= i < 8 and i not in password1:
            password1[i] = cod[6]

#soluzione 2
print(''.join([password1[k] for k in sorted(password1)]))
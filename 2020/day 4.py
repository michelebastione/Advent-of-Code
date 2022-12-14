import re

with open('input4.txt') as file:
    creds = file.read().split('\n\n')
    
fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
passports = []

for cred in creds:
    if all(field in cred for field in fields):
        passports.append(cred)
        
passports_with_separation = []
for passport in range(len(passports)):
    passports[passport] = passports[passport].split('\n')
    temp = []
    for section in passports[passport]:
        temp += section.split()
    passports_with_separation.append(temp)

passport_dicts = [{p.split(':')[0]:p.split(':')[1] for p in pp}
                  for pp in passports_with_separation]

valid_passports = 0
for passport in passport_dicts:
    if 1920<=int(passport['byr'])<=2002\
    and 2010<=int(passport['iyr'])<=2020\
    and 2020<=int(passport['eyr'])<=2030\
    and re.match(r'(1(([5-8]\d)|(9[0-3]))cm)|(((59)|(6\d)|(7[0-6]))in)', passport['hgt'])\
    and re.match(r'#[0-9a-f]{6}', passport['hcl'])\
    and passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']\
    and re.match(r'\d{9}$', passport['pid']):
        valid_passports += 1
        print(passport['pid'])
        
print(valid_passports)

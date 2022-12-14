import hashlib,re

md5 = lambda x: hashlib.md5(x.encode('utf-8')).hexdigest()

for i in range(10**8):
    if re.match(r'0{6,}', md5('bgvyzdsv'+str(i))):
        print(i)
        break

import numpy as np

diagonal_order = lambda y, x: ((x+y-1)*(x+y-2))//2 + x

count = 1
value = 20151125

while count < diagonal_order(3010, 3019):
    count += 1
    value = (value*252533) % 33554393

#soluzione 1
print(value)
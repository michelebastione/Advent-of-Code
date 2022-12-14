from sympy.ntheory import factorint, divisors

def sigma(n):
    prod = 1
    factors = factorint(n)
    for factor in factors:
        prod *= (factor**(factors[factor]+1)-1)//(factor-1)
    return prod

sigma_threshold = lambda x, y: sum(filter(lambda z: x//z < y, divisors(x)))

#soluzione 1
c=1
while sigma(c) < 3310000:
    c += 1
print(c)

#soluzione 2
c=1
while sigma_threshold(c, 50)*11 < 33100000:
    c += 1
print(c)
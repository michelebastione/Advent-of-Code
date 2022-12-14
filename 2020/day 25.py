card_public_key = 1614360
door_public_key = 7734663

def exponent_finder(base, modulo, key):
    loop = 1
    while pow(base, loop, modulo) != key:
        loop += 1
    return loop

# la soluzione è efficiente perché utilizza l'esponenziazione modulare della funzione pow()
card_loop = exponent_finder(7, 20201227, card_public_key)
print(pow(door_public_key, card_loop, 20201227))
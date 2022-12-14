import numpy as np

puzzle_input = 277678

def where_is(n):
    root = int(n**0.5)
    closest_odd_root = root if root%2==1 else root-1
    closest_square = closest_odd_root**2
    vertex_distance = n-closest_square
    side_distance = closest_odd_root//2+1
    x = vertex_distance%(side_distance*2)
    
    return side_distance+abs(x-side_distance+1)-1

#soluzione 1
print(where_is(puzzle_input))

def sum_adjacent(array, m, n):
    return sum(array[m-1: m+2, n-1: n+2])

spiral = np.zeros((100, 100), int)
current = [50, 50]
spiral[50, 50] = 1

count = 1
check = True
while check:
    for i in 0, 1:
        for j in range(count):
            current[i] += (-1)**(count-1)
            n, m = current
            spiral[m, n] = np.sum(spiral[m-1: m+2, n-1: n+2])
            if spiral[m, n] > puzzle_input:
                #soluzione 2
                print(spiral[m, n])
                check = False
                break
        if not check:
            break
    count += 1

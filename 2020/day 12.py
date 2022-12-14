with open('input12.txt') as file:
    data = file.read().splitlines()

instructions = [[i[0],i[1:]]for i in data]
direction = 'ENWS'

def rotate(string, offset, way):
    return [string[offset:]+string[:offset],
            string[len(string)-offset:]+string[:len(string)-offset]][way]

def normal_instructions(dirs):
    coordinates = [0, 0]
    move = {'N':'coordinates[0]+=','S':'coordinates[0]-=',
            'E':'coordinates[1]+=','W':'coordinates[1]-='}

    for instruction in instructions:
        if instruction[0] in move:
            exec(move[instruction[0]]+instruction[1])
        elif instruction[0] == 'L':
            dirs = rotate(dirs, (int(instruction[1])//90)%4, 0)
        elif instruction[0] == 'R':
            dirs = rotate(dirs, (int(instruction[1])//90)%4, 1)
        else:
            exec(move[dirs[0]]+instruction[1])
    return coordinates

def waypoint_instructions():
    coordinates = [0, 0]
    waypoint = [1, 10]
    move = {'N':'waypoint[0]+=','S':'waypoint[0]-=',
            'E':'waypoint[1]+=','W':'waypoint[1]-='}
    
    for instruction in instructions:
        w = waypoint
        n = (int(instruction[1])//90)%4
        if instruction[0] in move:
            exec(move[instruction[0]]+instruction[1])
        elif instruction[0] == 'L':
            waypoint = [[w[0],w[1],-w[0],-w[1]][n],
                        [w[1],-w[0],-w[1],w[0]][n]]
        elif instruction[0] == 'R':
            waypoint = [[w[0],-w[1],-w[0],w[1]][n],
                        [w[1],w[0],-w[1],-w[0]][n]]
        else:
            coordinates[0]+=waypoint[0]*int(instruction[1])
            coordinates[1]+=waypoint[1]*int(instruction[1])
            
    return coordinates    

#soluzione 1
ni = normal_instructions(direction)
print(abs(ni[0])+abs(ni[1]))

#soluzione 2
wi = waypoint_instructions()
print(abs(wi[0])+abs(wi[1]))

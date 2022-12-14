from copy import copy

with open('input22.txt') as file:
    p1, p2 = file.read().split('\n\n')

player_1 = [int(card) for card in p1.splitlines()[1:]]
player_2 = [int(card) for card in p2.splitlines()[1:]]

def combat(P1, P2):
    while len(P1) > 0 and len(P2) > 0:
        if P1[0] > P2[0]:
            P1 += [P1[0], P2[0]]
        else:
            P2 += [P2[0], P1[0]]
        del P1[0]
        del P2[0]
    return max(P1, P2)

#soluzione 1
winner = combat(copy(player_1), copy(player_2))[::-1]
print(sum(winner[n]*(n+1) for n in range(len(winner))))

def recursive_combat(P1, P2):
    rounds_p1 = []
    rounds_p2 = []
    while len(P1) > 0 and len(P2) > 0:
        if P1 in rounds_p1 or P2 in rounds_p2:
            return 0, P1
        else:
            rounds_p1.append(copy(P1))
            rounds_p2.append(copy(P2))
        if P1[0] < len(P1) and P2[0] < len(P2):
            winner = [P1, P2][recursive_combat(P1[1:P1[0]+1], P2[1:P2[0]+1])[0]]
            winner += [P1[0], P2[0]] if winner == P1 else [P2[0], P1[0]]
        else:
            if P1[0] > P2[0]:
                P1 += [P1[0], P2[0]]
            else:
                P2 += [P2[0], P1[0]]
        del P1[0]
        del P2[0]
    return (0, P1) if max(P1, P2) == P1 else (1, P2)

winner = recursive_combat(player_1, player_2)[1][::-1]
print(sum(winner[n]*(n+1) for n in range(len(winner))))
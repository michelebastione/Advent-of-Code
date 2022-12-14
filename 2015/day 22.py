class Wizard:
    def __init__(self, hp=50, mana=500, shield=0, poison=0, recharge=0):
        self.hp = hp
        self.mana = mana
        self.shield = shield
        self.poison = poison
        self.recharge = recharge

    def possible_moves(self):
        moves = []
        if self.mana >= 53:
            moves.append('m')
        if self.mana >= 73:
            moves.append('d')
        if self.mana >= 113 and self.shield == 0:
            moves.append('s')
        if self.mana >= 173 and self.poison == 0:
            moves.append('p')
        if self.mana >= 229 and self.recharge == 0:
            moves.append('r')
        return moves

class Game:
    def __init__(self, wizard, all_possible_manas, enemy_hp=51, mana_spent=0, hard=False):
        self.wiz = wizard
        self.enemy_hp = enemy_hp
        self.mana_spent = mana_spent
        self.hard = hard
        self.all_possible_manas = all_possible_manas

    def play(self):
        if not self.wiz.possible_moves():
            return

        new_games = []
        if self.hard:
            self.wiz.hp -= 1
            if self.wiz.hp <= 0:
                return

        if self.wiz.shield:
            self.wiz.shield -= 1
        if self.wiz.poison:
            self.wiz.poison -= 1
            self.enemy_hp -= 3
        if self.wiz.recharge:
            self.wiz.mana += 101
            self.wiz.recharge -= 1

        for i in self.wiz.possible_moves():
            new_enemy = self.enemy_hp
            new_hp = self.wiz.hp
            new_mana = self.wiz.mana
            new_shield = self.wiz.shield
            new_poison = self.wiz.poison
            new_recharge = self.wiz.recharge

            if i == 'm':
                updated_mana_spent = self.mana_spent + 53
                new_enemy = self.enemy_hp - 4
                new_mana -= 53
            elif i == 'd':
                updated_mana_spent = self.mana_spent + 73
                new_enemy = self.enemy_hp - 2
                new_hp += 2
                new_mana -= 73
            elif i == 's':
                updated_mana_spent = self.mana_spent + 113
                new_mana -= 113
                new_shield = 6
            elif i == 'p':
                updated_mana_spent = self.mana_spent + 173
                new_mana -= 173
                new_poison = 6
            else:
                updated_mana_spent = self.mana_spent + 229
                new_mana -= 229
                new_recharge = 5

            if new_poison:
                new_poison -= 1
                new_enemy -= 3
            if new_enemy <= 0:
                self.all_possible_manas.add(updated_mana_spent)
                continue

            if new_recharge:
                new_mana += 101
                new_recharge -= 1
            if new_shield:
                new_hp -= 2
                new_shield -= 1
            else:
                new_hp -= 9

            if new_hp <= 0 or any(m <= updated_mana_spent for m in self.all_possible_manas):
                continue

            new_wizard = Wizard(new_hp, new_mana, new_shield, new_poison, new_recharge)
            new_games.append(Game(new_wizard, self.all_possible_manas, new_enemy, updated_mana_spent, self.hard))

        for game in new_games:
            game.play()

#soluzione 1
game1 = Game(Wizard(), set())
game1.play()
print(min(game1.all_possible_manas))

#soluzione 2
game2 = Game(Wizard(), set(), hard=True)
game2.play()
print(min(game2.all_possible_manas))

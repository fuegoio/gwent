

class Board:
    def __init__(self, game, player):
        self.game = game
        self.player = player
        self.rows = [[], [], []]

    @property
    def scores(self):
        return [sum([card.power for card in row]) for row in self.rows]

    def __repr__(self):
        melee = f'      [Board] Melee : {self.rows[0]}'
        ranged = f'      [Board] Ranged : {self.rows[1]}'
        siege = f'      [Board] Siege : {self.rows[2]}'
        return melee + '\n' + ranged + '\n' + siege

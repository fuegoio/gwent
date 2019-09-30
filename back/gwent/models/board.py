

class Board:
    def __init__(self, game, player):
        self.game = game
        self.player = player
        self.rows = [[], [], []]

    @property
    def scores(self):
        return [sum([card.get_effective_power(self) for card in row]) for row in self.rows]

    def __repr__(self):
        scores = self.scores
        melee = f'      [Board] [{scores[0]}] Melee : {self.rows[0]}'
        ranged = f'      [Board] [{scores[1]}] Ranged : {self.rows[1]}'
        siege = f'      [Board] [{scores[2]}] Siege : {self.rows[2]}'
        return melee + '\n' + ranged + '\n' + siege

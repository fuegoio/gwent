class Board:
    def __init__(self, game, player):
        self.game = game
        self.player = player
        self.rows = [[], [], []]

    @property
    def scores(self):
        return [sum([card.get_effective_power(self) for card in row]) for row in self.rows]

    def delete_board(self, player):
        for row in self.rows:
            for card in row:
                card.destroy(self, player)

    def __repr__(self):
        scores = self.scores
        melee = f'      [Board] [{scores[0]}] Melee : {self.rows[0]}'
        ranged = f'      [Board] [{scores[1]}] Ranged : {self.rows[1]}'
        siege = f'      [Board] [{scores[2]}] Siege : {self.rows[2]}'
        return melee + '\n' + ranged + '\n' + siege

    def get_board_as_json(self, player):
        board = {'score_total': sum(self.scores)}
        for i in range(3):
            row = ['melee', 'distance', 'siege'][i]
            board[row] = {'cards': [card.get_data(self, player) for card in self.rows[i]],
                          'score': self.scores[i]}
        return board

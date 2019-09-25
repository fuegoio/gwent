import random

from gwent.data.cards import cards_db


class Board:
    def __init__(self, game, player):
        self.game = game
        self.player = player
        self.rows = [[], [], []]
        self.scores = [0, 0, 0]

    def update_scores(self):
        self.scores = [sum([card.power for card in row]) for row in self.rows]
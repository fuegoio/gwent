import random

from gwent.data.cards import cards_db


class Board:
    def __init__(self, game):
        self.game = game
        self.rows = []


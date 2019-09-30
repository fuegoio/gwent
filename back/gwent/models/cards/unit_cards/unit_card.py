import random

from gwent.models.cards.card import Card


class UnitCard(Card):
    def __init__(self, id: str, name: str, img_name: str, agile: bool, hero: bool, faction: str, power: int, row: int):
        super().__init__(id, name, img_name, faction)
        self.power = power
        self.agile = agile
        self.hero = hero
        self.row = row
        self.morale_boost = False

    def place_card(self, board, adversary_board, player, adversary):
        # to be overridden depending on abilities
        if self.agile:
            # Choose
            board.rows[random.randint(0, 1)].append(self)
        else:
            board.rows[self.row].append(self)
        self.apply_abilities(board, adversary_board, player, adversary)

    def apply_abilities(self, board, adversary_board, player, adversary):
        pass

    def get_effective_power(self, board):
        if self.hero:
            return self.power
        else:
            return self.power + self.get_morale_boost(board)

    def get_morale_boost(self, board):
        boost = -1 if self.morale_boost else 0
        for card in board.rows[self.row]:
            if card.morale_boost:
                boost += 1
        return boost

    def destroy(self, board, player):
        player.cemetery.append(self)
        board.rows[self.row].remove(self)

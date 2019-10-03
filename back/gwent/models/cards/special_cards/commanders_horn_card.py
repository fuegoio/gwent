import random
from gwent.models.cards.special_cards.special_card import SpecialCard


class CommandersHornCard(SpecialCard):
    def __repr__(self):
        return '<Commanders Horn>'

    def place_card(self, board, adversary_board, player, adversary):
        self.row = random.randint(0, 2)
        board.rows[self.row].append(self)

    def __init__(self, id: str, name: str, img_name: str, faction: str, row: int):
        super().__init__(id, name, img_name, faction, row)
        self.commanders_horn = True

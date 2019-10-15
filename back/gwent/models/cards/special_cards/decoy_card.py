import random

from gwent.models.cards.special_cards.special_card import SpecialCard
from gwent.models.cards.unit_cards.unit_card import UnitCard


class DecoyCard(SpecialCard):
    def __init__(self, id: str, name: str, img_name: str, faction: str, row: int):
        super().__init__(id, name, img_name, faction, row)
        self.type = 'decoy'

    def __repr__(self):
        return f'<Decoy {self.name}>'

    def get_targets(self, player, board):
        targets = []
        for row in board.rows:
            for card in row:
                if isinstance(card, UnitCard) and card.hero is False:
                    targets.append(card)
        print(targets)
        if len(targets) > 0:
            return targets
        else:
            return None

    def place_card(self, board, adversary_board, player, adversary, target):
        if isinstance(target, UnitCard):
            self.row = target.row
            player.hand.append(target)
            target.destroy(board, player)
            board.rows[self.row].append(self)
        else:
            self.row = random.randint(0, 2)
            board.rows[self.row].append(self)

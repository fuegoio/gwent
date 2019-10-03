import random

from gwent.models.cards.special_cards.special_card import SpecialCard
from gwent.models.cards.unit_cards.unit_card import UnitCard


class DecoyCard(SpecialCard):
    def __repr__(self):
        return f'<Decoy {self.name}>'

    def place_card(self, board, adversary_board, player, adversary):
        # when placed for another card, we change the value of the decoy's row
        # Random card replaced
        self.row = random.randint(0, 2)
        targetable = [card for card in board.rows[self.row] if isinstance(card, UnitCard) and self.hero is False]

        if len(targetable) > 0:
            card_replaced = targetable[random.randint(0, len(targetable) - 1)]
            player.hand.append(card_replaced)
            card_replaced.destroy(board, player)
            board.rows[self.row].append(self)
        else:
            board.rows[self.row].append(self)

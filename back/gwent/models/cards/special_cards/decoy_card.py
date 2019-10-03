import random

from gwent.models.cards.special_cards.special_card import SpecialCard


class DecoyCard(SpecialCard):
    def __repr__(self):
        return f'<Decoy {self.name}>'

    def place_card(self, board, adversary_board, player, adversary):
        # when placed for another card, we change the value of the decoy's row
        # Random card replaced
        self.row = random.randint(0, 2)

        if len(board.rows[self.row]) > 0:
            card_replaced = random.randint(0, len(board.rows[self.row]) - 1)
            player.hand.append(board.rows[self.row][card_replaced])
            board.rows[self.row][card_replaced].destroy(board, player)
            board.rows[self.row].append(self)
        else:
            board.rows[self.row].append(self)

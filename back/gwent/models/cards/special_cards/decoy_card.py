import random

from gwent.models.cards.special_cards.special_card import SpecialCard
from gwent.models.cards.unit_cards.unit_card import UnitCard


class DecoyCard(SpecialCard):
    def __repr__(self):
        return f'<Decoy {self.name}>'

    def get_row_and_targets(self, player, board):
        targets = []
        for row in board.rows:
            for card in row:
                if isinstance(card, UnitCard) and card.hero is False:
                    targets.append(card.id)
        if len(targets) > 0:
            return {'rows': [0, 1, 2], 'targets': {'target_type': 'decoy', 'target_ids': targets}}
        else:
            return {'rows': [0, 1, 2], 'targets': None}

    def place_card(self, board, adversary_board, player, adversary, target):
        targets = []
        for row in board.rows:
            for card in row:
                if isinstance(card, UnitCard) and card.hero is False:
                    targets.append(card)
        target_card = None
        if targets is not None:
            for card in targets:
                if card.id == target['target_id']:
                    target_card = card
                    break
        if isinstance(target_card, UnitCard):
            self.row = target_card.row
            player.hand.append(target_card)
            target_card.destroy(board, player, True)
            board.rows[self.row].append(self)
        else:
            print('Wrong target')

import random

from gwent.models.cards.unit_cards.unit_card import UnitCard


class MedicCard(UnitCard):
    def __repr__(self):
        return f'<Medic {self.img_name}>'

    def get_row_and_targets(self, player, board):
        revivable_units = [card for card in player.cemetery if card.hero is False and isinstance(card, UnitCard)]
        if len(revivable_units) > 0:
            print(revivable_units)
            print([card.id for card in revivable_units])
            return {'rows': [self.row],
                    'target': {'target_type': 'medic', 'target_ids': [card.id for card in revivable_units]}}
        else:
            return {'rows': [self.row], 'target': None}

    def apply_abilities(self, board, adversary_board, player, adversary, target):
        targets = self.get_row_and_targets(player, board)['target']
        target_card = None

        if targets is not None:
            for card in [card for card in player.cemetery if card.hero is False and isinstance(card, UnitCard)]:
                if card.id == target['target_id']:
                    target_card = card
                    break

        if target_card is not None:
            target_card.place_card(board, adversary_board, player, adversary, None)
        else:
            print('No cards revived by medic')

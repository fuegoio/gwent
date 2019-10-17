import random

from gwent.models.cards.unit_cards.unit_card import UnitCard


class MedicCard(UnitCard):
    def __repr__(self):
        return f'<Medic {self.img_name}>'

    def get_row_and_targets(self, player, board):
        revivable_units = [card for card in player.cemetery if card.hero is False and isinstance(card, UnitCard)]
        if len(revivable_units) > 0:
            return {'rows': [self.row], 'target': {'target_type': 'medic', 'target_ids': [card['id'] for card in revivable_units]}}
        else:
            return {'rows': [self.row], 'target': None}

    def apply_abilities(self, board, adversary_board, player, adversary, target: str = None):
        targets = self.get_row_and_targets(player, board)['target']
        target_card = None

        if targets is not None:
            for card in [card for card in player.cemetery if card.hero is False and isinstance(card, UnitCard)]:
                if card['id'] == target:
                    target_card = card
                    break

        if target_card is not None:
            if target_card.type != "medic":
                target_of_revived = None
                targets_of_revived = target_card.get_targets(player, board)
                if targets_of_revived is not None:
                    target_of_revived = targets_of_revived[random.randint(0, len(targets_of_revived) - 1)]
                target_card.place_card(board, adversary_board, player, adversary, target_of_revived)
            elif target_card is not None and target_card.type == "medic":
                target_card.place_card(board, adversary_board, player, adversary, None)
        else:
            print('Problem with target given to medic')


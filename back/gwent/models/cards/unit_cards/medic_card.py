import random

from gwent.models.cards.unit_cards.unit_card import UnitCard


class MedicCard(UnitCard):
    def __init__(self, id: str, name: str, img_name: str, agile: bool, hero: bool, faction: str, power: int, row: int):
        super().__init__(id, name, img_name, agile, hero, faction, power, row)
        self.type = 'medic'

    def __repr__(self):
        return f'<Medic {self.img_name}>'

    def get_targets(self, player, board):
        revivable = [card for card in player.cemetery if card.hero is False and isinstance(card, UnitCard)]
        if len(revivable) > 0:
            return revivable
        else:
            return None

    def apply_abilities(self, board, adversary_board, player, adversary, target: str = None):
        targets = self.get_targets(player, board)
        for card in targets:
            if card.id == target:
                target = card
                break
        if target is not None:
            if target.type != "medic":
                target_of_revived = None
                targets_of_revived = target.get_targets(player, board)
                if targets_of_revived is not None:
                    target_of_revived = targets_of_revived[random.randint(0, len(targets_of_revived) - 1)]
                target.place_card(board, adversary_board, player, adversary, target_of_revived)
            elif target is not None and target.type == "medic":
                target.place_card(board, adversary_board, player, adversary, None)
        else:
            pass


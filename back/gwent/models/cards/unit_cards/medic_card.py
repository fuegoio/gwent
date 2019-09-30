import random

from gwent.models.cards.unit_cards.unit_card import UnitCard


class MedicCard(UnitCard):
    def __repr__(self):
        return f'<Medic {self.img_name}>'

    def apply_abilities(self, board, adversary_board, player):
        if len(player.cemetery) > 0:
            random_card_number = random.randint(0, len(player.cemetery) - 1)
            player.cemetery[random_card_number].place_card(board, adversary_board, player)


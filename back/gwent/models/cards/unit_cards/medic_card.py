import random

from gwent.models.cards.unit_cards.unit_card import UnitCard


class MedicCard(UnitCard):
    def __repr__(self):
        return f'<Medic {self.img_name}>'

    def apply_abilities(self, board, adversary_board, player, adversary):
        revivable = [card for card in player.cemetery if card.hero is False and isinstance(card, UnitCard)]
        if len(revivable) > 0:
            random_card_number = random.randint(0, len(revivable) - 1)
            revivable[random_card_number].place_card(board, adversary_board, player, adversary)

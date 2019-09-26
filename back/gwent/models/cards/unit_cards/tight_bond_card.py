from gwent.models.cards.unit_cards.unit_card import UnitCard


class TightBondCard(UnitCard):
    def __init__(self):
        pass

    def apply_abilities(self, board, adversary_board, player):
        tight_bond_number = 0
        for card in board.rows[self.row]:
            if card.id == self.id:
                tight_bond_number += 1
        for card in board.rows[self.row]:
            if card.id == self.id:
                card.apply_tight_bond(tight_bond_number)

    def apply_tight_bond(self, unit_number):
        self.effective_power = self.power * unit_number


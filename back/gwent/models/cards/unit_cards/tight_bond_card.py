from gwent.models.cards.special_cards.weather_card import WeatherCard
from gwent.models.cards.unit_cards.unit_card import UnitCard


class TightBondCard(UnitCard):
    def __repr__(self):
        return f'<TightBond {self.img_name}>'

    def get_effective_power(self, board):
        tight_bond_number = 0
        for card in board.rows[self.row]:
            if card.img_name == self.img_name:
                tight_bond_number += 1
        bonuses = self.get_bonuses(board)
        if any(isinstance(x, WeatherCard) for x in board.rows[self.row]):
            return (tight_bond_number + bonuses['morale'])*bonuses['horn']
        else:
            return (self.power * tight_bond_number + bonuses['morale']) * bonuses['horn']

from gwent.models.cards.special_cards.weather_card import WeatherCard
from gwent.models.cards.unit_cards.unit_card import UnitCard


class TightBondCard(UnitCard):
    def __repr__(self):
        return f'<TightBond {self.img_name}>'

    def get_effective_power(self, board):
        tight_bond_number = 0
        for card in board.rows[self.row]:
            if card.id == self.id:
                tight_bond_number += 1

        if any(isinstance(x, WeatherCard) for x in board.rows[self.row]):
            return (tight_bond_number + self.get_morale_boost(board)) * self.get_commanders_horn(board)
        else:
            return (self.power * tight_bond_number + self.get_morale_boost(board)) * self.get_commanders_horn(board)


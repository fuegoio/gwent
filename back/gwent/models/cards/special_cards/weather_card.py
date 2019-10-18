from gwent.models.cards.special_cards.special_card import SpecialCard


class WeatherCard(SpecialCard):
    def __repr__(self):
        return f'<Weather {self.name}>'

    def place_card(self, board, adversary_board, player, adversary, target):
        for board in [board, adversary_board]:
            board.rows[self.row].append(self)

    def get_row_and_targets(self, player, board):
        return {'rows': [self.row], 'target': {'target_type': 'weather'}}

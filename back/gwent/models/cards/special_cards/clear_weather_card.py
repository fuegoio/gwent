from gwent.models.cards.special_cards.special_card import SpecialCard
from gwent.models.cards.special_cards.weather_card import WeatherCard


class ClearWeatherCard(SpecialCard):
    def get_row_and_targets(self, player, board):
        return {'rows': [0, 1, 2, 3, 4, 5], 'target': None}

    def place_card(self, board, adversary_board, player, adversary, target):
        self.apply_abilities(board, adversary_board, player, adversary)

    def apply_abilities(self, board, adversary_board, player, adversary):
        for board in [board, adversary_board]:
            for row in board.rows:
                for card in row:
                    if isinstance(card, WeatherCard):
                        card.destroy(board, player)

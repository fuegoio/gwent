from gwent.models.cards.special_cards.special_card import SpecialCard
from gwent.models.cards.special_cards.weather_card import WeatherCard


class ClearWeatherCard(SpecialCard):
    def __init__(self, name: str, img_name: str, faction: str, row: int):
        super().__init__(name, img_name, faction, row)
        self.type = 'clear_weather'

    def place_card(self, board, adversary_board, player, adversary, target):
        self.apply_abilities(board, adversary_board, player, adversary)

    def apply_abilities(self, board, adversary_board, player, adversary):
        for board in [board, adversary_board]:
            for row in board.rows:
                for card in row:
                    if isinstance(card, WeatherCard):
                        card.destroy(board, player)

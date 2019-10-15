from gwent.models.cards.special_cards.special_card import SpecialCard


class WeatherCard(SpecialCard):
    def __init__(self, id: str, name: str, img_name: str, faction: str, row: int):
        super().__init__(id, name, img_name, faction, row)
        self.type = 'weather'

    def __repr__(self):
        return f'<Weather {self.name}>'

    def place_card(self, board, adversary_board, player, adversary, target):
        for board in [board, adversary_board]:
            board.rows[self.row].append(self)

from gwent.models.cards.card import Card
from gwent.models.cards.special_cards.weather_card import WeatherCard


class UnitCard(Card):
    def __init__(self, id: str, name: str, img_name: str, agile: bool, hero: bool, faction: str, power: int, row: int):
        super().__init__(id, name, img_name, faction, row)
        self.power = power
        self.agile = agile
        self.hero = hero
        self.morale_boost = False
        self.type = ''

    def get_data(self, board=None):
        if board is None:
            return {
                'id': self.id,
                'name': self.name,
                'img_name': self.img_name,
                'agile': self.agile,
                'hero': self.hero,
                'row': self.row,
                'unit_card': True,
                'type': self.type
            }
        else:
            return {
                'id': self.id,
                'name': self.name,
                'img_name': self.img_name,
                'effective_power': self.get_effective_power(board),
                'agile': self.agile,
                'hero': self.hero,
                'row': self.row,
                'unit_card': True,
                'type': self.type
            }

    def get_targets(self, player, board):
        if self.agile:
            return [0, 1]
        else:
            return None

    def place_card(self, board, adversary_board, player, adversary, target):
        # to be overridden depending on abilities
        if self.agile:
            board.rows[target].append(self)
        else:
            board.rows[self.row].append(self)
        self.apply_abilities(board, adversary_board, player, adversary, target)

    def apply_abilities(self, board, adversary_board, player, adversary, target):
        pass

    def get_effective_power(self, board):
        if self.hero:
            return self.power * self.get_commanders_horn(board)
        elif any(isinstance(x, WeatherCard) for x in board.rows[self.row]):
            return (1 + self.get_morale_boost(board)) * self.get_commanders_horn(board)
        else:
            return (self.power + self.get_morale_boost(board)) * self.get_commanders_horn(board)

    # TODO : mix up get_moral_boost and get_commanders_horn method to check only once how to update the score
    def get_morale_boost(self, board):
        boost = -1 if self.morale_boost else 0
        for card in board.rows[self.row]:
            if isinstance(card, UnitCard):
                if card.morale_boost:
                    boost += 1
        return boost

    def get_commanders_horn(self, board):
        horn = 1
        for card in board.rows[self.row]:
            if card.commanders_horn:
                horn += 1
        return horn

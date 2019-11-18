from gwent.models.cards.card import Card
from gwent.models.cards.special_cards.weather_card import WeatherCard


class UnitCard(Card):
    def __init__(self, name: str, img_name: str, agile: bool, hero: bool, faction: str, power: int, row: int):
        super().__init__(name, img_name, faction, row)
        self.power = power
        self.agile = agile
        self.hero = hero
        self.morale_boost = False

    def get_data(self, board=None, player=None):
        data = {
            'id': self.id,
            'name': self.name,
            'img_name': self.img_name,
            'hero': self.hero,
            'unit_card': True,
        }

        if board is not None and player is not None:
            data['effective_power'] = self.get_effective_power(board)
            data['placement'] = self.get_row_and_targets(player, board)

        return data

    def get_row_and_targets(self, player, board):
        if self.agile:
            return {'rows': [0, 1], 'target': None}
        else:
            return {'rows': [self.row], 'target': None}

    def place_card(self, board, adversary_board, player, adversary, target):
        if not self.agile:
            board.rows[self.row].append(self)
        elif 0 <= target['row'] <= 1:
            self.row = target['row']
            board.rows[target['row']].append(self)
        else:
            print('Problem with agile target')
        self.apply_abilities(board, adversary_board, player, adversary, target)

    def apply_abilities(self, board, adversary_board, player, adversary, target):
        pass

    def get_effective_power(self, board):
        boost = self.get_bonuses(board)
        if self.hero:
            return self.power
        elif any(isinstance(x, WeatherCard) for x in board.rows[self.row]):
            return (1 + boost['morale']) * boost['horn']
        else:
            return (self.power + boost['morale']) * boost['horn']

    def get_bonuses(self, board):
        boost = {
            'morale': -1 if self.morale_boost else 0,
            'horn': 1
        }
        for card in board.rows[self.row]:
            if isinstance(card, UnitCard):
                if card.morale_boost:
                    boost['morale'] += 1
            if card.commanders_horn and boost['horn'] == 1:
                boost['horn'] = 2
        return boost

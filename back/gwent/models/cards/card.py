class Card:
    __card_id = 0

    def __init__(self, name: str, img_name: str, faction: str, row: int):
        self.id = Card.__card_id
        Card.__card_id += 1
        self.name = name
        self.img_name = img_name
        self.faction = faction
        self.power = 0
        self.row = row
        self.commanders_horn = False
        self.hero = False

    def __repr__(self):
        return f'<Card {self.img_name}>'

    def get_row_and_targets(self, player, board):
        return {'rows': [self.row], 'target': None}

    def place_card(self, board, adversary_board, player, adversary, target):
        pass

    def destroy(self, board, player, exclude_from_cemetery=False):
        try:
            if not exclude_from_cemetery:
                player.cemetery.append(self)
            board.rows[self.row].remove(self)
        except ValueError:
            print("No more cards to remove !")

    def get_effective_power(self, board):
        return self.power

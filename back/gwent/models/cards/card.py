class Card:
    def __init__(self, id: str, name: str, img_name: str, faction: str, row: int):
        self.id = id
        self.name = name
        self.img_name = img_name
        self.faction = faction
        self.power = 0
        self.row = row
        self.commanders_horn = False
        self.hero = False

    def __repr__(self):
        return f'<Card {self.img_name}>'

    def get_targets(self, player, board):
        return None

    def place_card(self, board, adversary_board, player, adversary, target):
        pass

    def destroy(self, board, player):
        try:
            player.cemetery.append(self)
            board.rows[self.row].remove(self)
        except ValueError:
            print("No more cards to remove !")

    def get_effective_power(self, board):
        return self.power

from gwent.models.cards.card import Card


class UnitCard(Card):
    def __init__(self, id: str, name: str, img_name: str, hero: bool, faction: str, power: int, row: int):
        super().__init__(id, name, img_name, faction)
        self.power = power
        self.effective_power = power
        self.hero = hero
        self.row = row

    def __repr__(self):
        return f'<Card {self.img_name}>'

    def place_card(self, board, adversary_board, player):
        # to be overridden depending on abilities
        board.rows[self.row].append(self)
        self.apply_abilities(board, adversary_board, player)

    def apply_abilities(self, board, adversary_board, player):
        # to be overridden depending on abilities
        pass

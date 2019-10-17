from gwent.models.cards.unit_cards.unit_card import UnitCard


class SpyCard(UnitCard):
    def __init__(self, name: str, img_name: str, agile: bool, hero: bool, faction: str, power: int, row: int):
        super().__init__(name, img_name, agile, hero, faction, power, row)
        self.type = 'spy'

    def __repr__(self):
        return f'<Spy {self.img_name}>'

    def place_card(self, board, adversary_board, player, adversary, target):
        adversary_board.rows[self.row].append(self)
        self.apply_abilities(board, adversary_board, player, adversary, target)

    def apply_abilities(self, board, adversary_board, player, adversary, target):
        player.draw_card()
        player.draw_card()


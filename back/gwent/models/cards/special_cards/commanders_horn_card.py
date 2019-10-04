from gwent.models.cards.special_cards.special_card import SpecialCard


class CommandersHornCard(SpecialCard):
    def __repr__(self):
        return '<Commanders Horn>'

    def get_targets(self, player, board):
        return [0, 1, 2]

    def place_card(self, board, adversary_board, player, adversary, target):
        self.row = target
        board.rows[self.row].append(self)

    def __init__(self, id: str, name: str, img_name: str, faction: str, row: int):
        super().__init__(id, name, img_name, faction, row)
        self.commanders_horn = True

from gwent.models.cards.card import Card


class SpecialCard(Card):
    def __init__(self, id: str, name: str, img_name: str, faction: str, row: int):
        super().__init__(id, name, img_name, faction)
        self.power = 0
        self.row = row

    def place_card(self, board, adversary_board, player, adversary):
        # to be overridden depending on abilities
        board.rows[self.row].append(self)
        self.apply_abilities(board, adversary_board, player, adversary)

    def apply_abilities(self, board, adversary_board, player, adversary):
        pass

    def destroy(self, board, player):
        try:
            board.rows[self.row].remove(self)
        except ValueError:
            print("No more cards to remove !")
from gwent.models.cards.card import Card


class SpecialCard(Card):
    def place_card(self, board, adversary_board, player, adversary, target):
        # to be overridden depending on abilities
        board.rows[self.row].append(self)
        self.apply_abilities(board, adversary_board, player, adversary)

    def apply_abilities(self, board, adversary_board, player, adversary):
        pass

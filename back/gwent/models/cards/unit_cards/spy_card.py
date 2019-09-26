from gwent.models.cards.unit_cards.unit_card import UnitCard


class SpyCard(UnitCard):
    def place_card(self, board, adversary_board, player):
        adversary_board.rows[self.row].append(self)
        self.apply_abilities(board, adversary_board, player)

    def apply_abilities(self, board, adversary_board, player):
        player.draw_card()
        player.draw_card()


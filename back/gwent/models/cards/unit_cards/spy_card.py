from gwent.models.cards.unit_cards.unit_card import UnitCard


class SpyCard(UnitCard):
    def __repr__(self):
        return f'<Spy {self.img_name}>'

    def place_card(self, board, adversary_board, player, adversary):
        adversary_board.rows[self.row].append(self)
        self.apply_abilities(board, adversary_board, player, adversary)

    def apply_abilities(self, board, adversary_board, player, adversary):
        player.draw_card()
        player.draw_card()


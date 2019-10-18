from gwent.models.cards.unit_cards.unit_card import UnitCard


class SpyCard(UnitCard):
    def __repr__(self):
        return f'<Spy {self.img_name}>'

    def place_card(self, board, adversary_board, player, adversary, target):
        adversary_board.rows[self.row].append(self)
        self.apply_abilities(board, adversary_board, player, adversary, target)

    def apply_abilities(self, board, adversary_board, player, adversary, target):
        player.draw_card()
        player.draw_card()

    def get_row_and_targets(self, player, board):
        return {'rows': [self.row + 3], 'target': None}

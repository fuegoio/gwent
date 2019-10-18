from gwent.models.cards.card import Card


class SpecialCard(Card):
    def get_data(self, board=None, player=None):
        if board is None or player is None:
            return {
                'id': self.id,
                'name': self.name,
                'img_name': self.img_name,
                'unit_card': False,
            }
        else:
            return {
                'id': self.id,
                'name': self.name,
                'img_name': self.img_name,
                'unit_card': False,
                'placement': self.get_row_and_targets(player, board)
            }

    def place_card(self, board, adversary_board, player, adversary, target):
        board.rows[self.row].append(self)
        self.apply_abilities(board, adversary_board, player, adversary)

    def apply_abilities(self, board, adversary_board, player, adversary):
        pass

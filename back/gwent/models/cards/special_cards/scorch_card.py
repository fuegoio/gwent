from gwent.models.cards.unit_cards import UnitCard
from gwent.models.cards.special_cards.special_card import SpecialCard


class ScorchCard(SpecialCard):
    def __init__(self, id: str, name: str, img_name: str, faction: str, row: int):
        super().__init__(id, name, img_name, faction, row)
        self.type = 'scorch'

    def place_card(self, board, adversary_board, player, adversary, target):
        self.apply_abilities(board, adversary_board, player, adversary)

    def apply_abilities(self, my_board, adversary_board, player, adversary):
        max_power = 0
        for board in [my_board, adversary_board]:
            for row in board.rows:
                for card in row:
                    if isinstance(card, UnitCard) and card.hero is False and card.get_effective_power(board) > max_power:
                        max_power = card.get_effective_power(board)
        for board in [my_board, adversary_board]:
            for row in board.rows:
                for card in row:
                    if isinstance(card, UnitCard) and max_power == card.get_effective_power(board) and card.hero is False:
                        card.destroy(board, board.player)

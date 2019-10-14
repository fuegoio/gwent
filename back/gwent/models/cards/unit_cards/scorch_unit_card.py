from gwent.models.cards.unit_cards.unit_card import UnitCard


class ScorchUnitCard(UnitCard):
    def __init__(self, id: str, name: str, img_name: str, agile: bool, hero: bool, faction: str, power: int, row: int):
        super().__init__(id, name, img_name, agile, hero, faction, power, row)
        self.type = 'scorch'

    def __repr__(self):
        return f'<Scorch {self.img_name}>'

    def apply_abilities(self, board, adversary_board, player, adversary, target):
        max_power = 0
        for card in adversary_board.rows[self.row]:
            if card.get_effective_power(adversary_board) > max_power and card.hero is False:
                max_power = card.get_effective_power(adversary_board)

        for card in adversary_board.rows[self.row]:
            if 0 < max_power == card.get_effective_power(adversary_board) and card.hero is False:
                card.destroy(adversary_board, adversary)

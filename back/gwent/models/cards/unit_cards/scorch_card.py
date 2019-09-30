from gwent.models.cards.unit_cards.unit_card import UnitCard


class ScorchCard(UnitCard):
    def __repr__(self):
        return f'<Scorch {self.img_name}>'

    def apply_abilities(self, my_board, adversary_board, player):
        max_power = 0
        for card in adversary_board.rows[self.row]:
            if card.get_effective_power() > max_power:
                max_power = card.get_effective_power()
        for card in adversary_board.rows[self.row]:
            if 0 < max_power == card.get_effective_power():
                card.destroy()

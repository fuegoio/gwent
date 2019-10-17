from gwent.models.cards.unit_cards.unit_card import UnitCard


class MoraleBoostCard(UnitCard):
    def __init__(self, name: str, img_name: str, agile: bool, hero: bool, faction: str, power: int, row: int):
        super().__init__(name, img_name, agile, hero, faction, power, row)
        self.morale_boost = True

    def __repr__(self):
        return f'<MoraleBoost {self.img_name}>'


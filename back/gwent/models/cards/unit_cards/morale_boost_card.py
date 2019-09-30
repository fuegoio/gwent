from gwent.models.cards.unit_cards.unit_card import UnitCard


class MoraleBoostCard(UnitCard):
    def __repr__(self):
        return f'<MoraleBoost {self.img_name}>'

    def __init__(self, id: str, name: str, img_name: str, hero: bool, faction: str, power: int, row: int):
        super().__init__(id, name, img_name, hero, faction, power, row)
        self.morale_boost = True


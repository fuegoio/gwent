from gwent.models.cards.unit_cards.unit_card import UnitCard


class CommandersHornUnitCard(UnitCard):
    def __init__(self, name: str, img_name: str, agile: bool, hero: bool, faction: str, power: int, row: int):
        super().__init__(name, img_name, agile, hero, faction, power, row)
        self.commanders_horn = True

    def __repr__(self):
        return f'<Commander {self.img_name}>'

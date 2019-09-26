class Card:
    def __init__(self, name: str, img_name: str, hero: bool, faction: str, power: int, row: int):
        self.name = name
        self.img_name = img_name
        self.faction = faction
        self.power = power
        self.hero = hero
        self.row = row
        self.load_abilities()

    def __repr__(self):
        return f'<Card {self.img_name}>'

    def place_card(self, round):
        # to be overridden depending on abilities
        round.boards[round.turn % 2].rows[self.row].append(self)
        self.apply_abilities(round)

    def apply_abilities(self, round):
        # to be overridden depending on abilities
        pass

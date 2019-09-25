class Card:
    def __init__(self, name: str, faction: str, power: int, row: int):
        self.name = name
        self.faction = faction
        self.power = power
        self.row = row
        self.abilities = []
        self.load_abilities()

    def __repr__(self):
        return f'<Card {self.name}>'

    def load_abilities(self):
        pass

    def place_card(self, round):
        #to be overriden depending on abilities
        round.boards[round.turn % 2].rows[self.row].append(self)
        self.apply_abilies(round)

    def apply_abilies(self, round):
        # to be overriden depending on abilities
        pass
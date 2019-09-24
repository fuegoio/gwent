class Card:
    def __init__(self, name: str, faction):
        self.name = name
        self.faction = faction

        self.abilities = []
        self.load_abilities()

    def __repr__(self):
        return f'<Card {self.name}>'

    def load_abilities(self):
        pass
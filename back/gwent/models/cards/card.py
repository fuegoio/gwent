class Card:
    def __init__(self, name: str, img_name: str, faction: str):
        self.name = name
        self.img_name = img_name
        self.faction = faction

    def __repr__(self):
        return f'<Card {self.img_name}>'

    def place_card(self, round):
        pass

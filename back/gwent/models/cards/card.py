class Card:
    def __init__(self, id: str, name: str, img_name: str, faction: str):
        self.id = id
        self.name = name
        self.img_name = img_name
        self.faction = faction

    def __repr__(self):
        return f'<Card {self.img_name}>'

    def place_card(self, round):
        pass

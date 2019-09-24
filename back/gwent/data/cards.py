from gwent.models.card import Card


class CardsDb:
    def __init__(self, filename):
        self.filename = filename
        self.cards = [
            Card('arachas', 'monster'),
            Card('arachas', 'monster'),
            Card('botchling', 'monster'),
            Card('biting_frost', 'neutral')
        ]

    def query_cards_by_faction(self, faction):
        filtered_cards = []
        for card in self.cards:
            if card.faction == faction:
                filtered_cards.append(card)
        return filtered_cards

    @property
    def neutral_cards(self):
        neutral_cards = []
        for card in self.cards:
            if card.faction == 'neutral':
                neutral_cards.append(card)
        return neutral_cards

    def load_cards_from_file(self):
        # card_class = {'agile': AgileCard, 'default': Card}
        with open(self.filename) as file:
            pass


cards_db = CardsDb('cards.txt')

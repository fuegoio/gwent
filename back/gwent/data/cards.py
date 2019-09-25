import os
import csv

from gwent.models.card import Card


class CardsDb:
    def __init__(self, filename):
        self.filename = filename
        self.cards = []
        self.load_cards_from_file()

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
        with open(os.path.join(os.path.realpath(__file__).split('cards.py')[0], self.filename)) as file:
            csv_file_reader = csv.DictReader(file)
            for card in csv_file_reader:
                # All the heroes cards are not taken into account for now
                if int(card['type']) < 4:
                    self.cards.append(Card(card['name'], card['img'], card['faction'], int(card['power']), int(card['type']) - 1))
            print(self.cards)


cards_db = CardsDb('cards.csv')

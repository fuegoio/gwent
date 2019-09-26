import os
import csv

from gwent.models.cards.unit_cards.unit_card import UnitCard


class CardsDb:
    def __init__(self, card_filename, deck_filename):
        self.card_filename = card_filename
        self.deck_filename = deck_filename
        self.cards = []
        self.load_cards_from_file()

    def query_deck_by_faction(self, faction):
        deck = []
        with open(os.path.join("./gwent/data/", self.deck_filename)) as file:
            csv_file_reader = csv.DictReader(file)
            for cards in csv_file_reader:
                if cards[faction] != "":
                    card = self.find_loaded_card(cards[faction])
                    # Most special cards are not taken into account so we check if they can be found in the "database"
                    if card is not None:
                        deck.append(card)
        return deck

    def load_cards_from_file(self):
        with open(os.path.join("./gwent/data/", self.card_filename)) as file:
            csv_file_reader = csv.DictReader(file)
            for card in csv_file_reader:
                if int(card['type']) < 4:
                    # Card is a unit card
                    if 'hero' in card['ability'].split(','):
                        self.cards.append(UnitCard(card['name'], card['img'], True, card['faction'], int(card['power']), int(card['type']) - 1))
                    else:
                        self.cards.append(UnitCard(card['name'], card['img'], False, card['faction'], int(card['power']), int(card['type']) - 1))
            print(self.cards)

    def find_loaded_card(self, card_name):
        for card in self.cards:
            if card.img_name == card_name:
                return card
        return None


cards_db = CardsDb('cards.csv', 'decks.csv')

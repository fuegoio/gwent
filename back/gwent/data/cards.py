import os
import csv

from gwent.models.cards.unit_cards.scorch_card import ScorchCard
from gwent.models.cards.unit_cards.unit_card import UnitCard
from gwent.models.cards.unit_cards.morale_boost_card import MoraleBoostCard
from gwent.models.cards.unit_cards.medic_card import MedicCard
from gwent.models.cards.unit_cards.spy_card import SpyCard
from gwent.models.cards.unit_cards.tight_bond_card import TightBondCard

constructor_dic = {
    'tight_bond': TightBondCard,
    'spy': SpyCard,
    'medic': MedicCard,
    'morale_boost': MoraleBoostCard,
    'scorch': ScorchCard,
}


class CardsDb:
    def __init__(self, card_filename, deck_filename):
        self.card_filename = card_filename
        self.deck_filename = deck_filename
        self.cards = []
        self.load_cards_from_file()
        self.loaded_decks = {}
        for faction in ['northern', 'nilfgaardian', 'scoiatael', 'monster']:
            self.loaded_decks[faction] = self.make_deck_by_faction(faction)
            print(self.loaded_decks[faction])

    def query_deck_by_faction(self, faction):
        return self.loaded_decks[faction]

    def make_deck_by_faction(self, faction):
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
                print(card['ability'])
                if int(card['type']) < 3:
                    # Card is a unit card
                    if 'hero' in card['ability'].split(','):
                        if card['ability'] == 'hero':
                            self.cards.append(UnitCard(card['id'], card['name'], card['img'], True, card['faction'], int(card['power']), int(card['type'])))
                        else:
                            pass
                            # self.cards.append()
                    else:
                        self.cards.append(UnitCard(card['id'], card['name'], card['img'], False, card['faction'], int(card['power']), int(card['type'])))
            print(self.cards)

    def find_loaded_card(self, card_id):
        for card in self.cards:
            if card.id == card_id:
                return card
        print('Card not found ' + card_id)
        return None


cards_db = CardsDb('cards.csv', 'decks.csv')

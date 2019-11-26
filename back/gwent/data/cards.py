import os
import csv

from gwent.models.cards import *

constructor_dic = {
    'tight_bond': TightBondCard,
    'spy': SpyCard,
    'medic': MedicCard,
    'morale_boost': MoraleBoostCard,
    'scorch': ScorchUnitCard,
    'muster': MusterCard,
    'hero': UnitCard,
    'commanders_horn': CommandersHornUnitCard,
    'agile': UnitCard,
    '': UnitCard,
    'weather': WeatherCard,
    'decoy': DecoyCard,
    'scorch_card': ScorchCard,
    'weather_clear': ClearWeatherCard,
    'commanders_horn_card': CommandersHornCard,
}


class CardsDb:
    def __init__(self, card_filename, deck_filename):
        self.card_filename = card_filename
        self.deck_filename = deck_filename

    def make_deck_by_faction(self, faction):
        deck = []
        with open(os.path.join("./gwent/data/", self.deck_filename)) as file:
            csv_file_reader = csv.DictReader(file)
            for cards in csv_file_reader:
                if cards[faction] != "":
                    new_card = self.make_card(cards[faction])
                    if new_card is not None:
                        deck.append(new_card)
                    else:
                        print('Card is None')
        return deck

    def make_card(self, card_id):
        with open(os.path.join("./gwent/data/", self.card_filename)) as file:
            csv_file_reader = csv.DictReader(file)
            new_card = None
            for line in csv_file_reader:
                if line['id'] == card_id:
                    if int(line['type']) < 3:
                        if 'weather' in line['ability'].split('_'):
                            new_card = constructor_dic['weather'](
                                line['name'],
                                line['img'],
                                line['faction'],
                                int(line['type'])
                            )
                        elif len(line['ability'].split(',')) >= 2:
                            new_card = constructor_dic[line['ability'].split(',')[1]](
                                line['name'],
                                line['img'],
                                'agile' in line['ability'].split(','),
                                'hero' in line['ability'].split(','),
                                line['faction'],
                                int(line['power']),
                                int(line['type'])
                            )
                        else:
                            new_card = constructor_dic[line['ability']](
                                line['name'],
                                line['img'],
                                'agile' in line['ability'].split(','),
                                'hero' in line['ability'].split(','),
                                line['faction'],
                                int(line['power']),
                                int(line['type'])
                            )
                    elif int(line['type']) == 3:
                        new_card = None
                    else:
                        new_card = constructor_dic[line['ability']](
                            line['name'],
                            line['img'],
                            line['faction'],
                            int(line['type'])
                        )
                    break
        return new_card


cards_db = CardsDb('cards.csv', 'decks.csv')

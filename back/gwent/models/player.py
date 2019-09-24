import random

from gwent.data.cards import cards_db

NUM_CARDS = 2
NUM_NEUTRAL_CARDS = 1


class Player:
    def __init__(self, name: str, faction: str):
        self.name = name
        self.faction = faction
        self.cards = []
        self.hand = []

    def pick_cards(self):
        cards_available = cards_db.query_cards_by_faction(self.faction)
        neutral_cards_available = cards_db.neutral_cards

        def pick_card(neutral=False):
            while True:
                if neutral:
                    random_card_number = random.randint(0, len(neutral_cards_available) - 1)
                    random_card = neutral_cards_available[random_card_number]
                else:
                    random_card_number = random.randint(0, len(cards_available) - 1)
                    random_card = cards_available[random_card_number]

                if random_card not in self.cards:
                    return random_card

        for i in range(NUM_CARDS):
            card = pick_card()
            self.cards.append(card)
            print(f'[Player] {self.name} picks card {card.name} !')

        for i in range(NUM_NEUTRAL_CARDS):
            neutral_card = pick_card(neutral=True)
            self.cards.append(neutral_card)
            print(f'[Player] {self.name} picks card {neutral_card.name} !')

    def draw_card(self):
        random_card_number = random.randint(0, len(self.cards) - 1)
        card = self.cards.pop(random_card_number)
        self.hand.append(card)

        print(f'[Player] {self.name} drew {card.name}')
        return card

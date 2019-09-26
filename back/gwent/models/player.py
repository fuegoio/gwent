import random

from gwent.data.cards import cards_db

NUM_CARDS = 30


class Player:
    def __init__(self, name: str, faction: str):
        self.name = name
        self.faction = faction
        self.lives = 2
        self.cards = []
        self.hand = []
        self.cemetery = []
        self._passed = False

    def __repr__(self):
        return self.name

    def pick_cards(self):
        cards_available = cards_db.query_deck_by_faction(self.faction)

        def pick_card():
            while True:
                random_card_number = random.randint(0, len(cards_available) - 1)
                random_card = cards_available[random_card_number]
                if random_card not in self.cards:
                    return random_card

        for i in range(NUM_CARDS):
            card = pick_card()
            self.cards.append(card)
            print(f'[Player] {self.name} picks card {card.name} !')

    def draw_card(self):
        random_card_number = random.randint(0, len(self.cards) - 1)
        card = self.cards.pop(random_card_number)
        self.hand.append(card)

        print(f'[Player] {self.name} drew {card.name}')
        return card

    def select_card(self):
        if len(self.hand) > 0 and not self._passed:
            random_card_number = random.randint(0, len(self.hand) - 1)
            card = self.hand.pop(random_card_number)
            print(f'[Player] {self.name} selected card {card}')
            return card

    def pass_turn(self):
        self._passed = True

    def reset_turn(self):
        self._passed = False

    def get_passed(self):
        return self._passed

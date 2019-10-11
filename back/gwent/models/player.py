import random

from gwent.data.cards import cards_db

NUM_CARDS = 22


class Player:
    def __init__(self, name: str, faction: str):
        self.name = name
        self.muligan_count = 0
        self.faction = faction
        self.__lives = 2
        self.deck = []
        self.hand = []
        self.cemetery = []
        self.__passed = False
        self.ready = False

    def __repr__(self):
        return self.name

    def pick_cards(self):
        cards_available = cards_db.query_deck_by_faction(self.faction)
        print(cards_available)

        def pick_card():
            while True:
                random_card_number = random.randint(0, len(cards_available) - 1)
                random_card = cards_available[random_card_number]
                if random_card not in self.deck:
                    return random_card

        for i in range(NUM_CARDS):
            card = pick_card()
            self.deck.append(card)
            print(f'[Player] {self.name} picks card {card.name} !')

    def draw_card(self):
        random_card_number = random.randint(0, len(self.deck) - 1)
        card = self.deck.pop(random_card_number)
        self.hand.append(card)

        print(f'[Player] {self.name} drew {card.name}')
        return card

    def select_card(self):
        if len(self.hand) > 0 and not self.__passed:
            random_card_number = random.randint(0, len(self.hand) - 1)
            card = self.hand.pop(random_card_number)
            print(f'[Player] {self.name} selected card {card}')
            return card

    def pass_turn(self):
        self.__passed = True

    def reset_turn(self):
        self.__passed = False

    @property
    def passed(self):
        return self.__passed

    def lose(self):
        self.__lives -= 1
        return self.__lives

    @property
    def lives(self):
        return self.__lives

    def get_hand_as_json(self):
        return [card.get_data() for card in self.hand]

    def do_mulligan(self, id, round_number):
        if self.muligan_count > 2 or round_number != 1:
            print('Unauthorized mulligan')
            # Raise error
        else:
            card_to_mullian = None
            for card in self.hand:
                if card.id == id:
                    card_to_mullian = card
            if card_to_mullian is not None:
                self.deck.append(card_to_mullian)
                self.hand.remove(card_to_mullian)
                self.draw_card()
                self.muligan_count += 1
                print('Mulligan done correctly')
            else:
                print('Card not found')
                # Raise error
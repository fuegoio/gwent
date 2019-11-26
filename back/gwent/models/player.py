import random

from gwent.data.cards import cards_db
from gwent.errors import UnauthorizedActionError, CardNotFoundError

NUM_CARDS = 22


class Player:
    def __init__(self, name: str, faction: str):
        self.name = name
        self.faction = faction

        self.__lives = 2
        self.__mulligan_count = 0
        self.__passed = False
        self.__ready = False

        self.deck = []
        self.hand = []
        self.cemetery = []

    @property
    def passed(self):
        return self.__passed

    @property
    def lives(self):
        return self.__lives

    @property
    def ready(self):
        return self.__ready

    def __repr__(self):
        return self.name

    def get_hand_data(self, board=None):
        return [card.get_data(board, self) for card in self.hand]

    def get_cemetery_data(self):
        return [card.get_data() for card in self.cemetery]

    def set_ready(self):
        self.__ready = True

    def pick_cards(self):
        cards_available = cards_db.make_deck_by_faction(self.faction)
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

    def find_card_by_id(self, card_id):
        card = None
        for i, hand_card in enumerate(self.hand):
            if card is None and hand_card.id == card_id:
                card = self.hand.pop(i)
        print(f'[Player] {self.name} selected card {card}')
        return card

    def pass_turn(self):
        self.__passed = True

    def reset_turn(self):
        self.__passed = False

    def lose(self):
        self.__lives -= 1
        return self.__lives

    def do_mulligan(self, card_id, round_number):
        if self.__mulligan_count >= 2 or round_number != 0:
            if self.__mulligan_count >= 2:
                raise UnauthorizedActionError('Mulligan exhausted')
            else:
                raise UnauthorizedActionError('Not your turn')

        else:
            card_to_mulligan = None
            for card in self.hand:
                if card.id == card_id:
                    card_to_mulligan = card
            if card_to_mulligan is not None:
                self.deck.append(card_to_mulligan)
                self.hand.remove(card_to_mulligan)
                self.draw_card()

                self.__mulligan_count += 1
                print('Mulligan done correctly')
                return True
            else:
                raise CardNotFoundError(card_to_mulligan)

    def get_player_data(self):
        return {'name': self.name,
                'faction': self.faction,
                'lives': self.__lives,
                'hand_length': len(self.hand),
                'passed': self.__passed}

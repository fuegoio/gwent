import random

from gwent.models.player import Player

NUM_CARDS_HANDS = 2


class Row:
    pass


class Game:
    def __init__(self, player_one: Player, player_two: Player):
        self.players = (player_one, player_two)
        self.terminated = False

        self.rows = []

    def run(self):
        # Choix du deck
        for player in self.players:
            player.pick_cards()

        # Piocher cartes
        for i in range(NUM_CARDS_HANDS):
            for player in self.players:
                player.draw_card()

        turn = random.randint(0, 1)
        while not self.terminated:
            player = self.players[turn % 2]
            print(f'[Game] {player.name}\'s turn. His hand : {player.hand}')
            input()

            turn += 1

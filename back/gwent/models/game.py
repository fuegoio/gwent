from gwent.models.board import Board
from gwent.models.player import Player
from gwent.models.round import Round

NUM_CARDS_HANDS = 2


class Game:
    def __init__(self, player_one: Player, player_two: Player):
        self.players = (player_one, player_two)
        self.board = Board(self)

    @property
    def terminated(self):
        players_deads = [player.lives == 0 for player in self.players]
        return sum(players_deads) >= 1

    def run(self):
        # Choix du deck
        for player in self.players:
            player.pick_cards()

        # Piocher cartes
        for i in range(NUM_CARDS_HANDS):
            for player in self.players:
                player.draw_card()

        while not self.terminated:
            current_round = Round(self)
            current_round.run_round()

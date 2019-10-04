from gwent.models.player import Player
from gwent.models.round import Round

NUM_CARDS_HANDS = 10


class Game:
    game_id = 0

    def __init__(self, player_one: Player, player_two: Player):
        self.players = (player_one, player_two)
        self.winner = None
        self.loser = None
        Game.game_id += 1

    @property
    def terminated(self):
        players_deads = [player.lives == 0 for player in self.players]
        return sum(players_deads) >= 1

    def draw_decks(self):
        # Choix du deck
        for player in self.players:
            player.pick_cards()

        # Piocher cartes
        for i in range(NUM_CARDS_HANDS):
            for player in self.players:
                player.draw_card()
        return [player.hand for player in self.players]

    def run(self):
        while not self.terminated:
            current_round = Round(self)
            current_round.run_round()

        for player in self.players:
            if player.lives >= 1:
                self.winner = player
                print(f'[Game] Winner is : {self.winner} !')
            elif player.lives == 0:
                self.loser = player

        if self.winner is None:
            print(f'[Game] Draw !')

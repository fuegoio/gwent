import random

from gwent.models.player import Player
from gwent.models.round import Round

NUM_CARDS_HANDS = 10


class Game:
    game_id = 0

    def __init__(self, player_one: Player, player_two: Player):
        self.players = (player_one, player_two)
        self.game_id = Game.game_id
        Game.game_id += 1
        self.round_number = 0
        self.current_round = None
        self.first_player = random.randint(0, 1)

    def __repr__(self):
        return f'<Game {self.game_id}>'

    @property
    def finished(self):
        players_dead = [player.lives == 0 for player in self.players]
        return sum(players_dead) >= 1

    def get_score(self):
        return [sum(board.scores) for board in self.current_round.boards]

    def get_current_turn(self):
        if self.current_round is not None:
            return self.current_round.turn

    def draw_decks(self):
        # Pick deck
        for player in self.players:
            player.pick_cards()

        # Pick cards
        for i in range(NUM_CARDS_HANDS):
            for player in self.players:
                player.draw_card()

    def init_round(self):
        if self.current_round is not None:
            self.current_round.boards[0].delete_board(self.players[0])
            self.current_round.boards[1].delete_board(self.players[1])

        self.round_number += 1
        self.current_round = Round(self, self.first_player)
        self.first_player = 1 - self.first_player

    def finish_round(self):
        boards_score = self.get_score()
        losers = [self.players[i] for i, score in enumerate(boards_score) if score == min(boards_score)]
        for loser in losers:
            loser.lose()
            print(f'[Round] {loser.name} loses the round.')
        if not self.finished:
            self.init_round()

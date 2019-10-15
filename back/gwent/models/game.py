import random

from gwent.models.board import Board
from gwent.models.player import Player
from gwent.models.round import Round

NUM_CARDS_HANDS = 10


class Game:
    game_id = 0

    def __init__(self, player_one: Player, player_two: Player):
        self.players = (player_one, player_two)
        self.winner = None
        self.loser = None

        self.game_id = Game.game_id
        Game.game_id += 1
        self.round_number = 1
        self.current_round = None
        self.boards = [Board(self, player) for player in self.players]
        self.first_player = random.randint(0, 1)
        self.turn = 0

    def __repr__(self):
        return f'<Game {self.game_id}>'

    @property
    def terminated(self):
        players_deads = [player.lives == 0 for player in self.players]
        return sum(players_deads) >= 1

    def draw_decks(self):
        # Pick deck
        for player in self.players:
            player.pick_cards()

        # Pick cards
        for i in range(NUM_CARDS_HANDS):
            for player in self.players:
                player.draw_card()
        return [player.hand for player in self.players]

    def init_round(self):
        self.boards[0].delete_board(self.players[0])
        self.boards[1].delete_board(self.players[1])
        self.round_number += 1
        self.current_round = Round(self, self.first_player)
        self.turn = self.first_player
        self.first_player = 1 - self.first_player

    def play_turn(self, data):
        if self.current_round.finished:
            boards_score = self.get_score()
            losers = [self.game.players[i] for i, score in enumerate(boards_score) if score == min(boards_score)]
            for loser in losers:
                loser.lose()
                print(f'[Round] {loser.name} loses the round.')
            self.init_round()
        elif len(self.players[self.turn].hand) != 0:
            if data['action'] == 'pass':
                self.current_round.pass_turn()
            elif data['action'] == 'play_card':
                self.current_round.play_card(data)
        if sum([player.passed for player in self.players]) == 0:
            self.turn = 1 - self.turn

    def get_score(self):
        return [sum(board.scores) for board in self.boards]


import random

from gwent.models.board import Board


class Round:
    def __init__(self, game: 'Game', turn=None):
        print('[Round] New round')
        self.game = game
        self.turn = turn
        if self.turn is None:
            self.turn = random.randint(0, 1)
        self.boards = [Board(self, player) for player in game.players]
        self.losers = None

        for player in self.game.players:
            player.reset_turn()

    @property
    def finished(self):
        players_passed = [player.get_passed() for player in self.game.players]
        return sum(players_passed) == 2

    def run_round(self):
        while not self.finished:
            player = self.game.players[self.turn % 2]
            board = self.boards[self.turn % 2]
            print(f'[Game] {player.name}\'s turn. His hand : {player.hand}')

            card = player.select_card()
            if card is None:
                player.pass_turn()
                print(f'[Game] {player.name}\' passes his turn')
            else:
                card.place_card(self)
                print(f'{board}')
            self.turn += 1

        # Define winner
        boards_score = [sum(board.scores) for board in self.boards]
        self.losers = [self.game.players[i] for i, score in enumerate(boards_score) if score == min(boards_score)]
        for loser in self.losers:
            loser.lives -= 1
            print(f'[Round] {loser.name} loses the round.')

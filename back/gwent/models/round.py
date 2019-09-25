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
        self.winner = None
        self.loser = None

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
                for board in self.boards:
                    board.update_scores()
                print(f'{board}')
            self.turn += 1

        # Define winner
        self.winner = self.game.players[0]
        self.loser = self.game.players[1]
        self.loser.lives -= 1

        print(f'[Round] {self.winner.name} wins the round !')

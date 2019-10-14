import random

from gwent.models.board import Board


class Round:
    def __init__(self, game: 'Game', first_to_play: int = None):
        print('[Round] New round')
        self.game = game
        self.turn = 0
        if first_to_play is not None:
            self.turn = first_to_play

        self.losers = None

        for player in self.game.players:
            player.reset_turn()

    @property
    def finished(self):
        players_passed = [player.passed for player in self.game.players]
        return sum(players_passed) == 2

    def pass_turn(self):
        pass

    def play_card(self, data):
        pass

    def run_round(self):
        while not self.finished:
            player = self.game.players[self.turn % 2]
            adversary = self.game.players[(self.turn + 1) % 2]
            board = self.boards[self.turn % 2]
            adversary_board = self.boards[(self.turn + 1) % 2]

            print(f'[Game] {player.name}\'s turn. His hand : {player.hand}')

            card = player.select_card()
            if card is None:
                player.pass_turn()
                print(f'[Game] {player.name}\' passes his turn')
            else:
                target = None
                targets = card.get_targets(player, board)
                if targets is not None and len(targets) > 0:
                    print(len(targets))
                    target = targets[random.randint(0, len(targets) - 1)]
                card.place_card(board, adversary_board, player, adversary, target)
                print(f'{board}')
            self.turn += 1

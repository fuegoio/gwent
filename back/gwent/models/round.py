import random

from gwent.models.board import Board


class Round:
    def __init__(self, game: 'Game', first_to_play: int):
        print('[Round] New round')
        self.game = game
        self.boards = [Board(self, player) for player in self.game.players]
        self.players = self.game.players
        self.turn = first_to_play

        self.losers = None

        for player in self.game.players:
            player.reset_turn()

    @property
    def finished(self):
        players_passed = [player.passed for player in self.players]
        return sum(players_passed) == 2

    def pass_turn(self):
        player = self.players[self.turn % 2]
        print(f'[Game] {player.name}\' passes his turn')
        self.toggle_turn()

    def play_card(self, data):
        player = self.players[self.turn % 2]
        adversary = self.players[(self.turn + 1) % 2]
        board = self.boards[self.turn % 2]
        adversary_board = self.boards[(self.turn + 1) % 2]

        print(f'[Game] {player.name}\'s turn. His hand : {player.hand}')
        card = player.find_card_by_id(data['id'])
        if card is not None:
            card.place_card(player, adversary, board, adversary_board, data['target'])
            self.toggle_turn()
        else:
            print('Card not found')

    def toggle_turn(self):
        if sum([player.passed for player in self.players]) == 0:
            self.turn = 1 - self.turn

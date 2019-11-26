from gwent.models.board import Board
from gwent.errors import CardNotFoundError


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
        player = self.players[self.turn]
        adversary = self.players[1 - self.turn]
        print(f'[Game] {player.name}\' passes his turn')
        player.pass_turn()
        if len(adversary.hand) == 0:
            adversary.pass_turn()
            print(f'[Game] {adversary.name}\' passes his turn')
        self.toggle_turn(adversary)

    def toggle_turn(self, adversary):
        if not adversary.passed:
            self.turn = 1 - self.turn

    def check_players_hand(self):
        for player in self.players:
            if len(player.hand) == 0:
                player.pass_turn()

    def play_card(self, card_id, target):
        player = self.players[self.turn]
        adversary = self.players[1 - self.turn]
        board = self.boards[self.turn]
        adversary_board = self.boards[1 - self.turn]

        print(f'[Game] {player.name}\'s turn. His hand : {player.hand}')
        card = player.find_card_by_id(card_id)
        if card is not None:
            card.place_card(board, adversary_board, player, adversary, target)

            self.check_players_hand()
            self.toggle_turn(adversary)
        else:
            raise CardNotFoundError(card)

import random


class Round:
    def __init__(self, game, turn=None):
        print('[Round] New round')
        self.game = game
        self.turn = turn
        if self.turn is None:
            self.turn = random.randint(0, 1)

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
            print(f'[Game] {player.name}\'s turn. His hand : {player.hand}')

            card = player.play_card()
            if card is None:
                player.pass_turn()

            self.turn += 1

        # Define winner
        self.winner = self.game.players[0]
        self.loser = self.game.players[1]
        self.loser.lives -= 1

        print(f'[Round] {self.winner.name} wins the round !')

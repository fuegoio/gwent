from gwent.models.game import Game
from gwent.models.player import Player


class GamesDb:
    def __init__(self):
        self.games_by_player = {}

    def launch_game(self, name1: str, faction1: str, name2: str, faction2: str) -> Game:
        player1 = Player(name1, faction1)
        player2 = Player(name2, faction2)
        game = Game(player1, player2)
        return game


games_db = GamesDb()

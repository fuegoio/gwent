from gwent.models.game import Game
from gwent.models.player import Player


class GamesDb():
    def __init__(self):
        self.games = {}

    def launch_game(self, name1: str, faction1: str, name2: str, faction2: str):
        id = Game.game_id + 1
        player1 = Player(name1, faction1)
        player2 = Player(name2, faction2)
        self.games[id] = Game(player1, player2)
        return id


games_db = GamesDb()

from gwent.models.game import Game
from gwent.models.player import Player


def create_game(player_one_name, player_two_name):
    player_one = Player(player_one_name, 'monster')
    player_two = Player(player_two_name, 'monster')

    game = Game(player_one, player_two)

    return game

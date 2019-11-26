import logging
import random

import socketio

FACTIONS = ['northern', 'nilfgaardian', 'scoiatael', 'monster']

sio = socketio.Client()
me = None
games = []


class GameAI(socketio.ClientNamespace):
    def __init__(self, namespace):
        super().__init__(str(namespace))
        self.mulligan = True
        self.hand = None
        self.turn = None

    def on_connect(self):
        print('connected')
        self.emit('get_cards')

    def on_hand(self, data):
        if self.mulligan:
            self.emit('ready_to_play')
            self.mulligan = False
        self.hand = data['hand']

    def on_board(self, data):
        self.turn = data['turn']
        if self.turn:
            self.emit('pass')


@sio.event
def available_players(data):
    players = [p['username'] for p in data['available_users']]
    print(f'Players available : {players}')
    global me
    me = [p for p in data['available_users'] if p['id'] == sio.sid][0]


@sio.event
def game_proposal(data):
    player = data['player'][0]
    print(f'Accepting player invite of player {player}')
    player['faction'] = FACTIONS[random.randint(0, len(FACTIONS) - 1)]
    me['faction'] = FACTIONS[random.randint(0, len(FACTIONS) - 1)]
    sio.emit('launch_game', {'player1': player, 'player2': me})


@sio.event
def game_created(data):
    global games

    namespace = data['namespace']
    game_socket = socketio.Client()
    game = GameAI(namespace)
    game_socket.register_namespace(game)
    game_socket.connect(f'http://localhost:3000/')


def connect():
    sio.connect('http://localhost:3000')
    sio.emit('register', {'username': 'Michel (AI)'})


if __name__ == '__main__':
    connect()

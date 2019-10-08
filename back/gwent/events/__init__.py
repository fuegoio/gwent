from gwent.data.games import GamesDb
from gwent.data.games import games_db
from .game import GameNamespace
import random


def register_events(sio):
    registered_users = []

    @sio.event
    def connect(sid, data):
        print(f'{sid} just connected')

    @sio.event
    async def register(sid, data):
        already_registered = False
        for user in registered_users:
            already_registered = already_registered or user['id'] == sid
        if not already_registered:
            registered_users.append({'id': sid, 'username': data['username'], 'available': True})
        print(registered_users)
        await sio.emit('available_players', {'available_users': registered_users, 'registered': sid})

    @sio.event
    async def propose_game(sid, data):
        await sio.emit('game_proposal', {'player': [user for user in registered_users if user['id'] == sid]}, data['adversary_id'])

    @sio.event
    async def refuse_game(sid, data):
        await sio.emit('game_refused', {}, data['proposer'])

    @sio.event
    async def launch_game(sid, data):
        print('Launching game')
        if random.randint(0, 2) == 0:
            player1 = data['player1']
            player2 = data['player2']
        else:
            player2 = data['player1']
            player1 = data['player2']
        game_id = games_db.launch_game(player1['username'], player1['faction'], player2['username'], player2['faction'])
        sio.register_namespace(GameNamespace(game_id))
        await sio.emit('game_created', {'id': game_id}, player1['id'])
        await sio.emit('game_created', {'id': game_id}, player2['id'])

    @sio.event
    async def disconnect(sid):
        for user in registered_users:
            if user['id'] == sid:
                registered_users.remove(user)
        await sio.emit('available_players', {'available_users': registered_users, 'registered': sid})


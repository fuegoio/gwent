from .game import GameNamespace


def register_events(sio):
    registered_users = []

    @sio.event
    def connect(sid, data):
        pass

    @sio.event
    async def register(sid, data):
        already_registered = False
        for user in registered_users:
            already_registered = already_registered or user['id'] == sid
            user['available'] = True
        if not already_registered:
            registered_users.append({'id': sid, 'username': data['username'], 'available': True})
        await sio.emit('available_players', {'available_users': registered_users, 'registered': sid})

    @sio.event
    async def propose_game(sid, data):
        await sio.emit('game_proposal', {'player': [user for user in registered_users if user['id'] == sid]},
                       data['adversary_id'])

    @sio.event
    async def refuse_game(sid, data):
        await sio.emit('game_refused', {}, data['proposer'])

    @sio.event
    async def launch_game(sid, data):
        player1 = data['player1']
        player2 = data['player2']
        game_namespace = GameNamespace(player1, player2)
        sio.register_namespace(game_namespace)
        for player in registered_users:
            if player['id'] == player1['id'] or player['id'] == player2['id']:
                player['available'] = False
        await sio.emit('available_players', {'available_users': registered_users})
        await sio.emit('game_created', {'namespace': game_namespace.game_id}, to=player1['id'])
        await sio.emit('game_created', {'namespace': game_namespace.game_id}, to=player2['id'])

    @sio.event
    async def disconnect(sid):
        for user in registered_users:
            if user['id'] == sid:
                registered_users.remove(user)
        await sio.emit('available_players', {'available_users': registered_users, 'registered': sid})

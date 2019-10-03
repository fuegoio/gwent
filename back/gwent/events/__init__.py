from .defaults import DefaultNamespace


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
        pass

    @sio.event
    async def disconnect(sid):
        for user in registered_users:
            if user['id'] == sid:
                registered_users.remove(user)
        await sio.emit('available_players', {'available_users': registered_users, 'registered': sid})

    sio.register_namespace(DefaultNamespace('/default'))

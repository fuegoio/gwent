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
        await sio.emit('available_players', {'available_users': [user for user in registered_users if user['available']]})

    @sio.event
    def disconnect(sid):
        for user in registered_users:
            if user['id'] == sid:
                registered_users.remove(user)
        print(f'{sid} just disconnected')

    sio.register_namespace(DefaultNamespace('/default'))

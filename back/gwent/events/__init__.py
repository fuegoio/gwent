from .defaults import DefaultNamespace


def register_events(sio):
    connected_users = []
    @sio.event
    def connect(sid, env):
        connected_users.append(sid)
        print(f'{len(connected_users)} users connected, {sid} just connected')

    @sio.event
    def register(sid, env):
        print('Received registration from front-end')

    @sio.event
    def disconnect(sid):
        connected_users.remove(sid)
        print(f'{len(connected_users)} users connected, {sid} just disconnected')

    sio.register_namespace(DefaultNamespace('/default'))

from .defaults import DefaultNamespace


def register_events(sio):
    @sio.event
    def connect(sid, env):
        print('connect ', sid)

    @sio.event
    def connected(sid):
        print('Received connected from front-end')

    @sio.event
    def disconnect(sid):
        print('disconnect ', sid)

    sio.register_namespace(DefaultNamespace('/default'))

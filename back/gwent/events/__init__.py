from .defaults import DefaultNamespace


def register_events(sio):
    @sio.event
    def connect(sid, environ):
        print('connect ', sid)

    @sio.event
    def disconnect(sid):
        print('disconnect ', sid)

    sio.register_namespace(DefaultNamespace('/default'))

import socketio

from gwent.events import register_events


def create_app():
    sio = socketio.AsyncServer(async_mode='asgi')
    register_events(sio)

    app = socketio.ASGIApp(sio)

    return app

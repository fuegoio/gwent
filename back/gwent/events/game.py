import socketio
from gwent.data.games import games_db

class GameNamespace(socketio.AsyncNamespace):
    def __init__(self, id):
        super().__init__(f'/{id}')
        self.id = id

    def on_connect(self, sid, environ):
        print('coucou')
        self.emit('connected')

    def on_connected(self, sid, environ):
        print('front end connected')

    def on_disconnect(self, sid):
        print('test')
        self.emit('test')

    async def on_michel(self, sid, data):
        await self.emit('my_response', data)

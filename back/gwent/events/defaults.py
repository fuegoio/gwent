import socketio


class DefaultNamespace(socketio.AsyncNamespace):
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

import socketio


class DefaultNamespace(socketio.AsyncNamespace):
    def on_connect(self, sid, environ):
        print('coucou')
        self.emit('coucou')

    def on_disconnect(self, sid):
        print('test')
        self.emit('test')

    async def on_michel(self, sid, data):
        await self.emit('my_response', data)

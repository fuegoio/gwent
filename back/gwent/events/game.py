import socketio

from gwent.data.games import games_db


class GameNamespace(socketio.AsyncNamespace):
    def __init__(self, id):
        super().__init__(f'/{id}')
        self.id = id
        self.game = games_db.get_by_id(id)

    async def on_draw_cards(self, sid, environ):
        print('Drawing cards')

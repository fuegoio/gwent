import socketio

from gwent.data.games import games_db


class GameNamespace(socketio.AsyncNamespace):
    def __init__(self, player1: dict, player2: dict):
        name1 = player1['username']
        name2 = player2['username']
        faction1 = player1['faction']
        faction2 = player2['faction']

        self.game = games_db.launch_game(name1, faction1, name2, faction2)
        self.game_id = self.game.game_id

        super().__init__(f'/{self.game_id}')

        self.players_token = (player1['id'], player2['id'])
        self.players_sid = [None, None]

    def get_player_from_sid(self, sid):
        for i, player_sid in enumerate(self.players_sid):
            if sid == player_sid:
                return self.game.players[i]

    async def on_connect(self, sid, environ):
        query_string = environ['QUERY_STRING']
        queries = query_string.split('&')
        token = None
        for query in queries:
            query_name, query_value = query.split('=')
            if query_name == 'token':
                token = query_value

        player = None
        for i, player_token in enumerate(self.players_token):
            if token == player_token:
                self.players_sid[i] = sid
                player = self.game.players[i]
                break

        print(f'Player {player} connected on namespace')

    async def on_disconnect(self, sid):
        for i, player_sid in enumerate(self.players_sid):
            if player_sid == sid:
                self.players_sid[i] = None
                break

        if len([sid for sid in self.players_sid if sid is not None]) == 0:
            print('Deleting namespace ...')
            del self.server.namespace_handlers[self.namespace]

    async def on_michel(self, sid, data):
        print(f'Michel {sid}')

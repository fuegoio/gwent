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

    def add_player_sid(self, sid, token):
        for i, player_token in enumerate(self.players_token):
            if token == player_token:
                self.players_sid[i] = sid
                return self.game.players[i]

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

        player = self.add_player_sid(sid, token)
        print(f'Player {player} connected on namespace')

    async def on_michel(self, sid, data):
        print(f'Michel {sid}')

import socketio

from gwent.data.games import games_db
from gwent.errors import UnauthorizedActionError, CardNotFoundError


class GameNamespace(socketio.AsyncNamespace):
    def __init__(self, player1: dict, player2: dict):
        name1 = player1['username']
        name2 = player2['username']
        faction1 = player1['faction']
        faction2 = player2['faction']

        self.game = games_db.launch_game(name1, faction1, name2, faction2)
        self.game_id = self.game.game_id
        self.game.draw_decks()

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

    async def on_get_cards(self, sid):
        player = self.get_player_from_sid(sid)
        await self.emit('hand', {'hand': player.get_hand_data()}, sid)

    async def on_mulligan(self, sid, data):
        player = self.get_player_from_sid(sid)
        try:
            player.do_mulligan(data['id'], self.game.round_number)
        except UnauthorizedActionError as e:
            print(e.message)
        except CardNotFoundError as e:
            print(e.message)
        else:
            await self.emit('done_mulligan', {'hand': player.get_hand_data()}, sid)

    async def on_ready_to_play(self, sid):
        player = self.get_player_from_sid(sid)
        player.set_ready()

        print(f'{player.name} ready')

        if len([player for player in self.game.players if player.ready]) == 2:
            self.game.init_round()
            await self.broadcast_board()

    async def on_pass(self, sid):
        turn = self.game.get_current_turn()
        if sid == self.players_sid[turn]:
            current_round = self.game.current_round
            current_round.pass_turn()
            await self.check_finished()
            await self.broadcast_board()
        else:
            print('Wrong user')

    async def on_play_card(self, sid, data):
        turn = self.game.get_current_turn()

        if sid == self.players_sid[turn]:
            card = data['card']
            target = data['target']
            current_round = self.game.current_round
            try:
                current_round.play_card(card, target)
            except CardNotFoundError as e:
                print(e.message)
            await self.check_finished()
            await self.broadcast_board()
        else:
            print('Wrong user')

    async def check_finished(self):
        current_round = self.game.current_round
        if current_round.finished:
            self.game.finish_round()
            if self.game.finished:
                for i, player_sid in enumerate(self.players_sid):
                    await self.emit('finished', {'result': self.game.players[i].lives != 0}, player_sid)

    async def broadcast_board(self):
        for i, sid in enumerate(self.players_sid):
            players = self.game.current_round.players
            boards = self.game.current_round.boards
            data = {
                'player': players[i].get_player_data(),
                'adversary': players[1 - i].get_player_data(),
                'hand': players[i].get_hand_data(boards[i]),
                'cemetery': players[i].get_cemetery_data(),
                'board': boards[i].get_board_as_json(players[i]),
                'adversary_board': boards[1 - i].get_board_as_json(players[i - 1]),
                'turn': i == self.game.get_current_turn()
            }
            await self.emit('board', data, sid)

    async def on_disconnect(self, sid):
        for i, player_sid in enumerate(self.players_sid):
            if player_sid == sid:
                self.players_sid[i] = None
            else:
                print('player left')
                await self.emit('adversary disconnected', {}, player_sid)

        if len([sid for sid in self.players_sid if sid is not None]) == 0:
            print('Deleting namespace ...')
            del self.server.namespace_handlers[self.namespace]

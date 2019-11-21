<template>
    <div class="game-finder">
        <v-row class="fill-height" align="center" justify="center">
            <v-col cols="4" class="pa-5 mt-3" offset="1">
                <v-text-field v-model="username" placeholder="Username" outlined dark hide-details
                              :disabled="registered">
                    <template v-slot:append>
                        <v-fade-transition mode="out-in">
                            <v-progress-circular
                                    v-if="loading"
                                    size="24"
                                    width="2"
                                    color="orange"
                                    indeterminate
                            ></v-progress-circular>
                            <v-icon v-else-if="registered" color="green">
                                check
                            </v-icon>
                        </v-fade-transition>
                    </template>
                </v-text-field>

                <v-btn block style="margin-top: 20px" :disabled="username.length === 0" v-if="!registered"
                       @click="sign_in(username)">Connect
                </v-btn>

                <v-card
                        style="background-color: #3F3632; border-radius: 15px"
                        v-if="registered && users.length > 1"
                >
                    <p style="text-align: center; color: #05DC95;" class="mt-3">
                        Available users
                    </p>
                    <v-list-item two-line v-for="user in users.filter((user) => user.id !== sid)"
                                 :class="{'available_player': user['available'], 'in_game_player': !user['available']}"
                                 style="margin-top: 10px" :key="user.sid">
                        <v-list-item-content>
                            <v-list-item-title>{{user['username']}}</v-list-item-title>
                            <v-list-item-subtitle>{{user['available'] ? 'Available' : 'In game'}}
                            </v-list-item-subtitle>
                        </v-list-item-content>
                        <v-btn rounded :disabled="!user['available']" @click="propose_game(user)">PLay</v-btn>
                    </v-list-item>
                </v-card>
                <p style="text-align: center; color: #05DC95;"
                   v-else-if="registered && users.length === 1" class="mt-3">
                    No users logged in
                </p>
                <p style="text-align: center; color: #05DC95;" v-else class="mt-3">
                    Enter a username to access matchmaking
                </p>
            </v-col>
            <v-col cols="7">
                <v-img src="gwent_logo.gif" id="logo"/>
            </v-col>
        </v-row>

        <v-dialog v-model="game_proposal" max-width="30%">
            <v-card v-if="!proposer">
                <p style="text-align: center; padding: 15px; margin: 0" class="title">{{adversary['username']}} wants to
                    play with you!</p>
                <v-card-actions>
                    <div class="flex-grow-1"></div>
                    <v-btn color="#05DC95" text @click="refuse_game">
                        Disagree
                    </v-btn>
                    <v-btn color="#05DC95" text @click="launch_game">
                        Agree
                    </v-btn>
                </v-card-actions>
            </v-card>
            <v-card v-if="proposer">
                <v-container>
                    <p style="text-align: center; padding: 10px" class="title">Waiting for {{adversary['username']}} to
                        accept your invitation</p>
                    <v-progress-circular
                            style="margin-left: 40%; margin-right: 40%; width: 20%; margin-bottom: 30px"
                            indeterminate
                            color="#05DC95"
                    ></v-progress-circular>
                </v-container>
            </v-card>
        </v-dialog>

        <v-snackbar v-model="snackbar" :timeout="2000">
            Game proposal refused
            <v-btn color="#05DC95" text @click="snackbar = false">Close</v-btn>
        </v-snackbar>
    </div>
</template>

<script>
    import io from 'socket.io-client';
    import sockets from '../plugins/sockets';

    export default {
        name: "GameFinder",
        data: () => ({
            loading: false,
            username: "",
            sid: "",
            registered: false,
            users: [],
            game_proposal: false,
            proposer: false,
            yourself: {},
            adversary: {},
            snackbar: false
        }),
        beforeCreate() {
            this.$sockets.main.on('connect', () =>  {
                this.sid = this.$sockets.main.id;
            });

            this.$sockets.main.on('available_players', (data) => {
                console.log(data);
                if (data['registered'] === this.sid) {
                    console.log('client registered')
                    this.registered = true
                }
                this.users = data['available_users'];
                for (let i = 0; i < this.users.length; i++) {
                    if (this.users[i]['id'] === this.sid) {
                        this.yourself = this.users[i]
                    }
                }
                this.users = data['available_users'];
                setTimeout(() => {
                    this.loading = false
                }, 1000);
            });

            this.$sockets.main.on('game_proposal', (data) => {
                this.adversary = data['player'][0];
                this.game_proposal = true
            });

            this.$sockets.main.on('game_refused', () => {
                this.game_proposal = false;
                this.snackbar = true
            });

            this.$sockets.main.on('game_created', (data) => {
                this.game_proposal = false;
                sockets.game = io(process.env.VUE_APP_API_URL + data.namespace, {query: {token: this.sid}, forceNew: true});
                this.$router.push('/game');
            });
        },
        methods: {
            sign_in(username) {
                this.loading = true;
                this.$sockets.main.emit('register', {'username': username});
            },
            propose_game(adversary) {
                console.log('Sending game proposal to ' + adversary['id']);
                this.game_proposal = true;
                this.proposer = true;
                this.adversary = adversary;
                this.$sockets.main.emit('propose_game', {adversary_id: adversary['id']})
            },
            launch_game() {
                this.game_proposal = false;
                this.adversary['faction'] = ['northern', 'nilfgaardian', 'scoiatael', 'monster'][Math.floor(Math.random() * 4)];
                this.yourself['faction'] = ['northern', 'nilfgaardian', 'scoiatael', 'monster'][Math.floor(Math.random() * 4)];
                this.$sockets.main.emit('launch_game', {
                    player1: this.adversary,
                    player2: this.yourself,
                })
            },
            refuse_game() {
                this.game_proposal = false;
                this.$sockets.main.emit('refuse_game', {refuser: this.sid, proposer: this.adversary['id']})
            }
        }
    }
</script>

<style scoped>
    .game-finder {
        height: 100%;
    }

    #logo {
        margin: auto;
        display: block;
    }

    .in_game_player {
        background-color: #dc6072;
        border-radius: 15px;
        margin-bottom: 5px;
        overflow-y: auto;
        max-height: 50%;
    }

    .available_player {
        background-color: #05DC95;
        border-radius: 15px;
        margin-bottom: 5px;
        overflow-y: auto;
        max-height: 50%;
    }
</style>

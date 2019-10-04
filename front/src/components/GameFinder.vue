<template>
    <v-layout class="full-height" row>
        <v-flex class="full-height" style="margin-top: auto; margin-bottom: auto" xs4>
            <v-container id="side-bar">
                <v-text-field v-model="username" placeholder="Username" outlined dark hide-details :disabled="registered"></v-text-field>
                <v-btn block style="margin-top: 20px" :disabled="username.length == 0" v-if="!registered" @click="sign_in">Connect</v-btn><br><br>
                <v-card
                  style="background-color: #3F3632; border-radius: 15px"
                  class="mx-auto"
                  v-if="registered && users.length > 0"
                >
                  <v-list-item two-line v-for="user in users" class="list-item" v-if="sid != user['id']">
                    <v-list-item-content>
                      <v-list-item-title>{{user['username']}}</v-list-item-title>
                      <v-list-item-subtitle>{{user['available'] ? 'Available' : 'In game'}}</v-list-item-subtitle>
                    </v-list-item-content>
                    <v-btn rounded :disabled="!user['available']" @click="propose_game(user)">PLay</v-btn>
                  </v-list-item>
                </v-card>
                <p v-if="!registered" style="text-align: center; color: #05DC95;">Enter a username to access matchmaking</p>
                <p v-if="registered && users.length == 0" style="text-align: center; color: #05DC95;">No users logged in</p>
            </v-container>
        </v-flex>
        <v-flex class="full-height" xs8>
            <img src="gwent_logo.gif" id="logo">
        </v-flex>
        <v-dialog v-model="game_proposal" max-width="30%">
            <v-card v-if="!proposer">
                <p style="text-align: center; padding: 15px; margin: 0" class="title">{{adversary['username']}} wants to play with you!</p>
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
                    <p style="text-align: center; padding: 10px" class="title">Waiting for {{adversary['username']}} to accept your invitation</p>
                    <v-progress-circular
                            style="margin-left: 40%; margin-right: 40%; width: 20%; margin-bottom: 30px"
                        indeterminate
                        color="#05DC95"
                    ></v-progress-circular>
                </v-container>
            </v-card>
        </v-dialog>
        <v-snackbar
            v-model="snackbar"
            :timeout="2000"
        >
            Game proposal refused
        <v-btn color="#05DC95" text @click="snackbar = false">Close</v-btn>
      </v-snackbar>
    </v-layout>
</template>

<script>
    export default {
        name: "GameFinder",
        data: () => ({
            username: "",
            sid: "",
            registered: false,
            users: [],
            game_proposal: false,
            proposer: false,
            adversary: [],
            snackbar: false
        }),
        sockets: {
            connect(){
                this.sid = this.$socket.id
            },
            available_players(data) {
                console.log(data)
                if (data['registered'] == this.sid) {
                    this.registered = true
                }
                this.users = data['available_users']
                console.log(this.users)
            },
            game_proposal(data) {
                this.adversary = data['player'][0]
                this.game_proposal = true
            },
            game_refused() {
                this.game_proposal = false
                this.snackbar = true
            }
        },
        methods: {
            sign_in() {
                this.$socket.emit('register', {'username': this.username})
            },
            propose_game(adversary) {
                console.log('Sending game proposal to ' + adversary['id'])
                this.game_proposal = true
                this.proposer = true
                this.adversary = adversary
                this.$socket.emit('propose_game', {adversary_id: adversary['id']})
            },
            launch_game() {
                this.$router.push('/game')
                this.game_proposal = true
                const faction1 = ['northern', 'nilfgaardian', 'scoiatael', 'monster'][Math.floor(Math.random() * Math.floor(4))]
                const faction2 = ['northern', 'nilfgaardian', 'scoiatael', 'monster'][Math.floor(Math.random() * Math.floor(4))]
                this.$socket.emit('launch_game', {name1: this.username, faction1: faction1, name2: this.adversary['username'], faction2: faction2})
            },
            refuse_game() {
                this.game_proposal = false
                this.$socket.emit('refuse_game', {refuser: this.sid, proposer: this.adversary['id']})
            }
        }
    }
</script>

<style scoped>
    .full-height {
        height: 100%;
    }
    #logo {
        position: absolute;
        top: 0;
        bottom: 0;
        margin: auto;
    }
    #side-bar {
        padding: 20px;
        margin-top: 20%;
    }
    .list-item {
        background-color: #05DC95;
        border-radius: 15px;
        margin-bottom: 5px;
        overflow-y: auto;
        max-height: 50%;
    }
</style>
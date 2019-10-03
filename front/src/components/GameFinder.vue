<template>
    <v-layout class="full-height" row>
        <v-flex class="full-height" style="margin-top: auto; margin-bottom: auto" xs4>
            <v-container id="side-bar">
                <v-text-field v-model="username" placeholder="Username" outlined dark hide-details :disabled="registered"></v-text-field>
                <v-btn block style="margin-top: 20px" :disabled="username.length == 0" v-if="!registered" @click="sign_in">Connect</v-btn><br><br>
                <v-card
                  style="background-color: #3F3632"
                  class="mx-auto"
                  tile
                  v-if="registered && users.length > 0"
                >
                  <v-list-item two-line v-for="user in users" class="list-item" v-if="sid != user['id']">
                    <v-list-item-content>
                      <v-list-item-title>{{user['username']}}</v-list-item-title>
                      <v-list-item-subtitle>{{user['available'] ? 'Available' : 'In game'}}</v-list-item-subtitle>
                    </v-list-item-content>
                    <v-btn :disabled="!user['available']" @click="propose_game(user)">Connect</v-btn>
                  </v-list-item>
                </v-card>
                <p v-if="!registered" class="title" style="text-align: center">Enter a username to access matchmaking</p>
                <p v-if="registered && users.length == 0" class="title" style="text-align: center">No users logged in</p>
            </v-container>
        </v-flex>
        <v-flex class="full-height" xs8>
            <img src="gwent_logo.gif" id="logo">
        </v-flex>
        <v-dialog v-model="game_proposal" max-width="290">
            <v-card v-if="!proposer">
                <v-card-title>{{adversary['username']}} wants to play with you!</v-card-title>
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
                <v-card-title>Waiting for {{adversary['username']}} to accept your invitation</v-card-title>
                <v-container style="margin-left: 40%; margin-right: 40%; width: 20%">
                    <v-progress-circular
                        indeterminate
                        color="#05DC95"
                    ></v-progress-circular>
                </v-container>
            </v-card>
        </v-dialog>
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
            adversary: []
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
                this.$socket.emit('launch_game', {accepter: this.sid, proposer: this.adversary['id']})
            },
            refuse_game() {
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
    }
    .list-item {
        background-color: #05DC95;
        border-radius: 15px;
        margin-bottom: 5px;
    }
    .title {
        color: #05DC95;
    }
</style>
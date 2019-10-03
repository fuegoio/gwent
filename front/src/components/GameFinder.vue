<template>
    <v-layout class="full-height" row>
        <v-flex class="full-height" style="margin-top: auto; margin-bottom: auto" xs4>
            <v-container id="side-bar">
                <v-text-field v-model="username" placeholder="Username" outlined dark hide-details></v-text-field>
                <v-btn block style="margin-top: 20px" :disabled="username.length == 0" @click="sign_in">Connect</v-btn><br><br>
                <v-card
                  style="background-color: #3F3632"
                  class="mx-auto"
                  tile
                  v-if="registered && users.length > 0"
                >
                  <v-list-item two-line v-for="user in users" class="list-item">
                    <v-list-item-content>
                      <v-list-item-title>{{user['username']}}</v-list-item-title>
                      <v-list-item-subtitle>{{user['available'] ? 'Available' : 'Not available'}}</v-list-item-subtitle>
                    </v-list-item-content>
                    <v-btn>Connect</v-btn>
                  </v-list-item>
                </v-card>
                <p v-if="!registered" class="title" style="text-align: center">Enter a username to access matchmaking</p>
                <p v-if="registered && users.length == 0" class="title" style="text-align: center">No users logged in</p>
            </v-container>
        </v-flex>
        <v-flex class="full-height" xs8>
            <img src="gwent_logo.gif" id="logo">
        </v-flex>
    </v-layout>
</template>

<script>
    export default {
        name: "GameFinder",
        data: () => ({
            username: "",
            registered: false,
            users: [],
        }),
        sockets: {
            available_players(data) {
                console.log('Getting players')
                this.registered = true
                this.users = data['available_users']
            }
        },
        methods: {
            sign_in() {
                this.$socket.emit('register', {'username': this.username})
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
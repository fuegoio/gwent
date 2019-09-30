<template>
    <v-layout class="full-height" row>
        <v-flex class="full-height" style="margin-top: auto; margin-bottom: auto" xs4>
            <v-container id="side-bar">
                <v-text-field v-model="username" placeholder="Username" outlined dark hide-details></v-text-field>
                <v-btn block style="margin-top: 20px" :disabled="username.length == 0" @click="sign_in">Connect</v-btn>
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
            username: ""
        }),
        methods: {
            sign_in(){
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
</style>
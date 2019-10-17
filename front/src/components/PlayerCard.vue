<template>
    <v-container class="player_card_back">
        <v-row>
            <v-col>{{player_name}}</v-col>
            <v-col>Total score : {{score}}</v-col>
        </v-row>
        <v-row>
            <v-col cols="1">{{length_hand}}
            </v-col>
            <v-col cols="1"><v-img :src="'./card_icon.png'" height="25px" contain></v-img></v-col>
            <v-col cols="6"></v-col>
            <v-col>Lives : {{player_lives}}</v-col>
        </v-row>
    </v-container>
</template>

<script>
    export default {
        name: "PlayerCard",
        components: {},
        props: ['player_name', 'player_lives', 'length_hand', 'score']
    }
</script>

<style scoped>
    .player_card_back{
        background-color: #05DC95;
        border-radius: 7px;
    }
</style>
<template>
    <div>
        <div v-if="!mulligan">
            <Row :cards="adversary_board['siege']" :description="false"></Row>
            <Row :cards="adversary_board['distance']" :description="false"></Row>
            <Row :cards="adversary_board['melee']" :description="false"></Row>
            <Row :cards="board['melee']" :description="false"></Row>
            <Row :cards="board['distance']" :description="false"></Row>
            <Row :cards="board['siege']" :description="false"></Row>
            <Row :cards="hand" :description="false"></Row>
        </div>

        <v-dialog v-model="mulligan" persistent>
            <v-layout column class="full-height" style="background-color: #3F3632">
                <v-progress-linear color="#3F3632" background-color="#05DC95" v-model="mulligan_chronometer"></v-progress-linear>
                <p style="color: #05DC95; text-align: center; margin-top: 10px">
                    Choose a card to redraw ({{mulligan_count}}/2)
                </p>
                <Row :cards="hand" :description="true" v-on:click="do_mulligan" :disabled="disable_mulligan"></Row>
                <v-btn :disabled="disable_mulligan" class="skip-button" style="background-color: #05DC95" @click="skip_mulligan">Skip</v-btn>
            </v-layout>
        </v-dialog>
    </div>
</template>

<script>
    import Row from "./Row"

    export default {
        name: "Board",
        components: {Row},
        data() {
            return {
                hand: [],
                board: {
                    melee: [],
                    distance: [],
                    siege: []
                },
                adversary_board: {
                    melee: [],
                    distance: [],
                    siege: []
                },
                cemetery: [],
                turn: false,
                mulligan: false,
                disable_mulligan: false,
                mulligan_count: 0,
                mulligan_chronometer: 0,
            }
        },
        beforeCreate() {
            this.$sockets.game.on('hand', (data) => {
                console.log(data)
                this.hand = data['hand'];
                this.mulligan = true
                this.increment_chronometer()
            });

            this.$sockets.game.on('done_mulligan', (data) => {
                this.hand = data['hand'];
                this.mulligan_count += 1;
                if(this.mulligan_count >= 2){
                    this.disable_mulligan = true
                    setTimeout(() => {
                        this.mulligan = false
                        this.$sockets.game.emit('ready_to_play')
                    }, 1000);
                }
            })

            this.$sockets.game.on('board', (data) => {
                console.log(data)
                this.hand = data['hand'];
                this.board = data['board'];
                this.adversary_board = data['adversary_board'];
                this.cemetery = data['cemetery'];
                this.turn = data['turn']
            })
            this.$sockets.game.emit('get_cards');
        },
        methods: {
            increment_chronometer(){
                if(this.mulligan_chronometer < 100){
                    this.mulligan_chronometer += 0.5
                    setTimeout(() => {
                        this.increment_chronometer()
                    }, 100)
                } else if (this.mulligan) {
                    this.mulligan = false
                    this.$sockets.game.emit('ready_to_play');
                }
            },
            do_mulligan(id){
                if (this.mulligan_count < 2){
                    this.$sockets.game.emit('mulligan', id)
                }
            },
            skip_mulligan(){
                this.mulligan = false;
                this.$sockets.game.emit('ready_to_play');
            }
        }
    }
</script>

<style scoped>
    .full-height {
        height: 100%;
    }

    .skip-button {
        margin: 20px;
        color: white;
    }
</style>
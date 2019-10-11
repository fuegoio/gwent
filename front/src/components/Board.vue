<template>
    <div>
        <v-dialog v-model="mulligan" persistent>
            <v-layout column class="full-height" style="background-color: #3F3632">
                <v-progress-linear color="#3F3632" background-color="#05DC95" v-model="mulligan_chronometer"></v-progress-linear>
                <p style="color: #05DC95; text-align: center; margin-top: 10px">
                    Choose a card to redraw ({{mulligan_count}}/2)
                </p>
                <Row :cards="deck" :mulligan="true" v-on:click="do_mulligan"></Row>
                <v-btn class="skip-button" style="background-color: #05DC95" @click="skip_mulligan">Skip</v-btn>
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
                deck: [],
                mulligan: false,
                mulligan_count: 0,
                mulligan_chronometer: 0,
            }
        },
        beforeCreate() {
            this.$sockets.game.on('deck', (data) => {
                console.log(data['deck'])
                this.deck = data['deck'];
                this.mulligan = true
                this.increment_chronometer()
            });

            this.$sockets.game.on('done_mulligan', (data) => {
                this.deck = data['deck'];
                this.mulligan_count += 1;
                if(this.mulligan_count >= 2){
                    setTimeout(() => {
                        this.mulligan = false
                        this.$sockets.game.emit('ready_to_play')
                    }, 2000);
                }
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
                } else {
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
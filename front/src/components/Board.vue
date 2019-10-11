<template>
    <div>
        <v-dialog v-model="mulligan" persistent>
            <v-layout column class="full-height" style="background-color: #3F3632">
                <p style="color: #05DC95; text-align: center; margin-top: 10px">
                    Choose a card to redraw ({{mulligan_count}}/2)
                </p>
                <Row :cards="deck" :mulligan="true" v-on:click="do_mulligan"></Row>
                <v-btn class="skip-button" style="background-color: #05DC95">Skip</v-btn>
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
                mulligan_count: 0
            }
        },
        beforeCreate() {
            this.$sockets.game.on('deck', (data) => {
                console.log(data['deck'])
                this.deck = data['deck'];
                this.mulligan = true
            });

            this.$sockets.game.on('done_mulligan', (data) => {
                console.log(data['deck'])
                this.deck = data['deck'];
                this.mulligan_count += 1;
                if(this.mulligan_count >= 2){
                    setTimeout(() => {
                        this.mulligan = false
                    }, 1000);
                }
            })

            this.$sockets.game.emit('get_cards');
        },
        methods: {
            do_mulligan(id){
                console.log(id)
                this.$sockets.game.emit('mulligan', id)
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
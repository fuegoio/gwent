<template>
    <div>
        <v-dialog v-model="mulligan" persistent hide-overlay>
            <v-layout column class="full-height" style="background-color: #3F3632">
                <p style="color: #05DC95; text-align: center">
                    Choose a card to redraw ({{mulligan_count}}/2)
                </p>
                <Row :cards="deck" :mulligan="true"></Row>
                <v-btn  style="margin-top: 10px">Skip</v-btn>
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
                this.deck = data['deck'];
                this.mulligan = true
            });

            this.$sockets.game.on('mulligan', (data) => {
                this.deck = data['deck'];
                this.mulligan_count += 1;
                if(this.mulligan_count >= 2){
                    this.mulligan = false;
                }
            })

            this.$sockets.game.emit('get_cards');
        }
    }
</script>

<style scoped>
    .centered {
        text-align: center;
    }

    .full-height {
        height: 100%;
    }
</style>
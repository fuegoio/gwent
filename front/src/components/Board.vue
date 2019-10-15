<template>
    <div>
        <div v-if="!mulligan">
            <Row :cards="adversary_board['siege']" :number="5" :description="false" v-on:row_click="place_card"></Row>
            <Row :cards="adversary_board['distance']" :number="4" :description="false" v-on:row_click="place_card"></Row>
            <Row :cards="adversary_board['melee']" :number="3" :description="false" v-on:row_click="place_card"></Row>
            <Row :cards="board['melee']" :number="0" :description="false" v-on:row_click="place_card"></Row>
            <Row :cards="board['distance']" :number="1" :description="false" v-on:row_click="place_card"></Row>
            <Row :cards="board['siege']" :number="2" :description="false" v-on:row_click="place_card"></Row>
            <Row :cards="hand" :number="6" :description="false" v-on:card_click="select_card"></Row>
        </div>

        <v-dialog v-model="mulligan" persistent>
            <v-layout column class="full-height" style="background-color: #3F3632">
                <v-progress-linear color="#3F3632" background-color="#05DC95"
                                   v-model="mulligan_chronometer"></v-progress-linear>
                <p style="color: #05DC95; text-align: center; margin-top: 10px">
                    Choose a card to redraw ({{mulligan_count}}/2)
                </p>
                <Row :cards="hand" :description="true" v-on:mulligan="do_mulligan" :disabled="disable_mulligan"></Row>
                <v-btn :disabled="disable_mulligan" class="skip-button" style="background-color: #05DC95"
                       @click="skip_mulligan">Skip
                </v-btn>
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
                selected_card: null,
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
                disabled_rows: [true, true, true, true, true, true],
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

            this.$sockets.game.on('terminated', () => {
                console.log('Game is over')
            })

            this.$sockets.game.on('done_mulligan', (data) => {
                this.hand = data['hand'];
                this.mulligan_count += 1;
                if (this.mulligan_count >= 2) {
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
            select_card(card) {
                this.selected_card = card;
            },
            place_card(row_number) {
                if (this.selected_card != null && this.check_emplacement(row_number)) {
                    console.log('good placement')
                    this.$sockets.game.emit('play', {action: 'play_card', id: this.selected_card['id'], raw_number: row_number})
                } else {
                    this.selected_card = null
                }
            },
            increment_chronometer() {
                if (this.mulligan_chronometer < 100) {
                    this.mulligan_chronometer += 0.5
                    setTimeout(() => {
                        this.increment_chronometer()
                    }, 100)
                } else if (this.mulligan) {
                    this.mulligan = false
                    this.$sockets.game.emit('ready_to_play');
                }
            },
            do_mulligan(id) {
                if (this.mulligan_count < 2) {
                    this.$sockets.game.emit('mulligan', {id: id})
                }
            },
            skip_mulligan() {
                this.mulligan = false;
                this.$sockets.game.emit('ready_to_play');
            },
            check_emplacement(row_number) {
                if (this.selected_card['unit_card']) {
                    if (this.selected_card['agile']) {
                        return 0 <= row_number <= 1
                    } else if (this.selected_card['type'] == 'spy') {
                        return this.selected_card['row'] + 3 == row_number
                    } else {
                        return this.selected_card['row'] == row_number
                    }
                } else {
                    return false
                }
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
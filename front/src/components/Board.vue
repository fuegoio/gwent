<template>
    <div>
        <div>
            <Row :cards="adversary_board['siege']" :number="5" :description="false" v-on:row_click="place_card"></Row>
            <Row :cards="adversary_board['distance']" :number="4" :description="false" v-on:row_click="place_card"></Row>
            <Row :cards="adversary_board['melee']" :number="3" :description="false" v-on:row_click="place_card"></Row>
            <Row :cards="board['melee']" :number="0" :description="false" v-on:row_click="place_card"></Row>
            <Row :cards="board['distance']" :number="1" :description="false" v-on:row_click="place_card"></Row>
            <Row :cards="board['siege']" :number="2" :description="false" v-on:row_click="place_card"></Row>
            <Row :cards="hand" :number="6" :description="false" v-on:card_click="select_card" hand="true" :disabled="!turn"></Row>
        </div>

        <MulliganDialog :cards="hand"></MulliganDialog>

        <CemeteryDialog :cards="cemetery" :active="medic" v-on:card_click="choose_medic_target"></CemeteryDialog>
    </div>
</template>

<script>
    import Row from "./Row"
    import MulliganDialog from "./MulliganDialog";
    import CemeteryDialog from "./CemetaryDialog";

    export default {
        name: "Board",
        components: {Row, MulliganDialog, CemeteryDialog},
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
                turn: false,
                medic: false,
            }
        },
        beforeCreate() {
            this.$sockets.game.on('hand', (data) => {
                this.hand = data['hand'];
            });

            this.$sockets.game.on('terminated', () => {
                console.log('Game is over')
            })

            this.$sockets.game.on('done_mulligan', (data) => {
                this.hand = data['hand'];
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
                    if (this.selected_card['agile'] == true){
                        this.$sockets.game.emit('play_card', {card: this.selected_card['id'], target: row_number})
                    } else if (this.selected_card['type'] == 'medic') {
                        this.medic = true
                    } else {
                        this.$sockets.game.emit('play_card', {card: this.selected_card['id'], target: null})
                    }
                } else {
                    this.selected_card = null
                }
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
            },
            choose_medic_target(card){
                this.$sockets.game.emit('play_card', {card: this.selected_card['id'], target: card['id']})
                this.medic = false
            }
        }
    }
</script>

<style scoped>
    .full-height {
        height: 100%;
    }
</style>
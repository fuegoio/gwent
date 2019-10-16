<template>
    <div>
        <v-row class="adversory" no-gutters>
            <v-col cols="2" align-self="center" class="text-center">
                <v-chip>
                    {{ adversary_board['siege'].score }}
                </v-chip>
            </v-col>
            <v-col cols="10">
                <Row :cards="adversary_board['siege'].cards" :number="5" :description="false"
                     v-on:card_click="handle_card_click"
                     v-on:row_click="place_card"></Row>
            </v-col>
            <v-col cols="2" align-self="center" class="text-center">
                <v-chip>
                    {{ adversary_board['distance'].score }}
                </v-chip>
            </v-col>
            <v-col cols="10">
                <Row :cards="adversary_board['distance'].cards" :number="4" :description="false"
                     v-on:card_click="handle_card_click"
                     v-on:row_click="place_card"></Row>
            </v-col>
            <v-col cols="2" align-self="center" class="text-center">
                <v-chip>
                    {{ adversary_board['melee'].score }}
                </v-chip>
            </v-col>
            <v-col cols="10">
                <Row :cards="adversary_board['melee'].cards" :number="3" :description="false"
                     v-on:card_click="handle_card_click"
                     v-on:row_click="place_card"></Row>
            </v-col>
            <v-col cols="2" align-self="center" class="text-center">
                <v-chip>
                    {{ board['melee'].score }}
                </v-chip>
            </v-col>
            <v-col cols="10">
                <Row :cards="board['melee'].cards" :number="0" :description="false" v-on:row_click="place_card"
                     v-on:card_click="handle_card_click"></Row>
            </v-col>
            <v-col cols="2" align-self="center" class="text-center">
                <v-chip>
                    {{ board['distance'].score }}
                </v-chip>
            </v-col>
            <v-col cols="10">
                <Row :cards="board['distance'].cards" :number="1" :description="false"
                     v-on:card_click="handle_card_click"
                     v-on:row_click="place_card"></Row>
            </v-col>
            <v-col cols="2" align-self="center" class="text-center">
                <v-chip>
                    {{ board['siege'].score }}
                </v-chip>
            </v-col>
            <v-col cols="10">
                <Row :cards="board['siege'].cards" :number="2" :description="false" v-on:row_click="place_card"
                     v-on:card_click="handle_card_click"></Row>
            </v-col>
            <v-col cols="2" align-self="center" class="text-center">
                <v-chip>
                    Michel
                </v-chip>
            </v-col>
            <v-col cols="10">
                <Row :cards="hand" :number="6" :description="false" v-on:card_click="select_card" hand="true"
                     :disabled="!turn"></Row>
            </v-col>
        </v-row>

        <MulliganDialog :cards="hand"></MulliganDialog>

        <CemeteryDialog :cards="cemetery" :active="medic" v-on:card_click="choose_medic_target"></CemeteryDialog>
    </div>
</template>

<script>
    import Row from "./Row"
    import MulliganDialog from "./MulliganDialog";
    import CemeteryDialog from "./MedicDialog";

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
            });

            this.$sockets.game.on('done_mulligan', (data) => {
                this.hand = data['hand'];
            });

            this.$sockets.game.on('board', (data) => {
                console.log(data);
                this.hand = data['hand'];
                this.board = data['board'];
                this.adversary_board = data['adversary_board'];
                this.cemetery = data['cemetery'];
                this.turn = data['turn']
            });

            this.$sockets.game.emit('get_cards');
        },
        methods: {
            select_card(data) {
                this.selected_card = data['card'];
            },
            place_card(row_number) {
                if (this.selected_card != null && this.check_emplacement(row_number)) {
                    console.log('good placement')
                    if (this.selected_card['agile'] == true || this.selected_card['type'] == "commanders_horn") {
                        this.$sockets.game.emit('play_card', {
                            card: this.selected_card['id'],
                            target: row_number
                        })
                    } else if (this.selected_card['type'] == 'medic') {
                        if (this.any_card_revivable()) {
                            this.medic = true
                        } else {
                            this.$sockets.game.emit('play_card', {
                                card: this.selected_card['id'],
                                target: null
                            })
                        }
                    } else {
                        this.$sockets.game.emit('play_card', {
                            card: this.selected_card['id'],
                            target: null
                        })
                    }
                } else {
                    this.selected_card = null
                }
            },
            handle_card_click(data) {
                if (this.selected_card['type'] == 'decoy') {
                    this.$sockets.game.emit('play_card', {
                        card: this.selected_card['id'],
                        target: data['card']['id']
                    })
                } else {
                    this.place_card(data['row_number'])
                }
            },
            check_emplacement(row_number) {
                if (this.selected_card['agile']) {
                    return 0 <= row_number && row_number <= 1
                } else if (this.selected_card['type'] == 'spy') {
                    return this.selected_card['row'] + 3 == row_number
                } else if (this.selected_card['type'] == 'commanders_horn') {
                    return 0 <= row_number && row_number <= 2
                } else {
                    return this.selected_card['row'] == row_number
                }
            },
            choose_medic_target(card) {
                this.$sockets.game.emit('play_card', {card: this.selected_card['id'], target: card['id']})
                this.medic = false
            },
            any_card_revivable() {
                let revivable_card = 0
                for (let i = 0; i < this.cemetery.length; i++) {
                    if (this.cemetery[i]['unit_card'] && !this.cemetery[i]['hero']) {
                        revivable_card += 1
                    }
                }
                return revivable_card > 0
            }
        }
    }
</script>

<style scoped>
    .full-height {
        height: 100%;
    }
</style>
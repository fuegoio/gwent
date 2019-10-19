<template>
    <div>
        <v-row class="adversory" no-gutters>
            <v-col cols="3">
                <v-row no-gutters>
                    <PlayerCard :length_hand="adversary['hand_length']" :player_lives="adversary['lives']"
                                :player_name="adversary['name']" :score="adversary_board['score_total']">
                    </PlayerCard>
                </v-row>
                <v-row style="height: 220px;"></v-row>
                <v-btn height="60px" @click="pass_turn" :disabled="!turn">Pass</v-btn>
                <v-row style="height: 220px;"></v-row>
                <v-row no-gutters>
                    <PlayerCard :length_hand="player['hand_length']" :player_lives="player['lives']"
                                :player_name="player['name']" :score="board['score_total']">
                    </PlayerCard>
                </v-row>
            </v-col>
            <v-col cols="1">
                <v-row class="score" align-content="center" justify="center">
                    <v-chip>
                        {{adversary_board['siege']['score']}}
                    </v-chip>
                </v-row>
                <v-row class="score" align-content="center" justify="center">
                    <v-chip>
                        {{adversary_board['distance']['score']}}
                    </v-chip>
                </v-row>
                <v-row class="score" align-content="center" justify="center">
                    <v-chip>
                        {{adversary_board['melee']['score']}}
                    </v-chip>
                </v-row>
                <v-row class="score" align-content="center" justify="center">
                    <v-chip>
                        {{board['melee']['score']}}
                    </v-chip>
                </v-row>
                <v-row class="score" align-content="center" justify="center">
                    <v-chip>
                        {{board['distance']['score']}}
                    </v-chip>
                </v-row>
                <v-row class="score" align-content="center" justify="center">
                    <v-chip>
                        {{board['siege']['score']}}
                    </v-chip>
                </v-row>
            </v-col>
            <v-col cols="8">
                <Row :cards="adversary_board['siege'].cards" :number="5"
                     v-on:card_click="handle_card_click"
                     v-on:row_click="handle_row_click">
                </Row>
                <Row :cards="adversary_board['distance'].cards" :number="4"
                     v-on:card_click="handle_card_click"
                     v-on:row_click="handle_row_click">
                </Row>
                <Row :cards="adversary_board['melee'].cards" :number="3"
                     v-on:card_click="handle_card_click"
                     v-on:row_click="handle_row_click">
                </Row>
                <Row :cards="board['melee'].cards" :number="0" v-on:row_click="handle_row_click"
                     v-on:card_click="handle_card_click">
                </Row>
                <Row :cards="board['distance'].cards" :number="1"
                     v-on:card_click="handle_card_click"
                     v-on:row_click="handle_row_click">
                </Row>
                <Row :cards="board['siege'].cards" :number="2" v-on:row_click="handle_row_click"
                     v-on:card_click="handle_card_click">
                </Row>
            </v-col>
            <Row :cards="hand" :number="6" v-on:card_click="select_card" hand="true"
                 :disabled="!turn">
            </Row>
        </v-row>

        <MulliganDialog :cards="hand"></MulliganDialog>

        <MedicDialog :cards="cemetery" :active="medic" :ids="medic_ids" v-on:card_click="choose_medic_target"></MedicDialog>
    </div>
</template>

<script>
    import Row from "./Row"
    import MulliganDialog from "./MulliganDialog";
    import MedicDialog from "./MedicDialog";
    import PlayerCard from "./PlayerCard";

    export default {
        name: "Board",
        components: {Row, MulliganDialog, MedicDialog, PlayerCard},
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
                medic_ids: [],
                player: {
                    name: String,
                    faction: String,
                    lives: Number
                },
                adversary: {
                    name: String,
                    faction: String,
                    lives: Number
                },
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
                this.turn = data['turn'];
                this.player = data['player'];
                this.adversary = data['adversary']
            });

            this.$sockets.game.emit('get_cards');
        },
        methods: {
            select_card(data) {
                this.selected_card = data['card'];
            },
            handle_row_click(row_number) {
                const placement = this.selected_card['placement'];
                console.log(placement)
                if (this.selected_card != null && placement['rows'].includes(row_number)) {
                    if (placement['targets'] == null) {
                        this.$sockets.game.emit('play_card', {
                            card: this.selected_card['id'],
                            target: {row: row_number, target: null}
                        })
                    } else if (placement['targets']['target_type'] == 'medic') {
                        if (placement['targets']['target_ids'].length > 0) {
                            this.medic_ids = placement['targets']['target_ids'];
                            this.medic = true;
                        } else {
                            this.$sockets.game.emit('play_card', {
                                card: this.selected_card['id'],
                                target: {row: row_number, target: null}
                            })
                        }
                    }
                } else {
                    console.log('Wrong row selected');
                }
            },
            handle_card_click(data) {
                const targets = this.selected_card['placement']['targets']
                if (targets != null && targets['target_type'] == 'decoy') {
                    if (targets['target_ids'].includes(data['card']['id'])) {
                        this.$sockets.game.emit('play_card', {
                            card: this.selected_card['id'],
                            target: {row: data['row_number'], target_id: data['card']['id']}
                        })
                    } else {
                        console.log('Wrong decoy placement')
                    }
                } else {
                    this.handle_row_click(data['row_number'])
                }
            },
            choose_medic_target(card) {
                this.$sockets.game.emit('play_card', {
                    card: this.selected_card['id'],
                    target: {row: null, target_id: card['id']}
                });
                this.medic = false
                this.medic_ids = []
            },
            pass_turn() {
                this.$sockets.game.emit('pass')
            }
        }
    }
</script>

<style scoped>
    .score {
        height: 125px;
        text-align: center;
    }
</style>
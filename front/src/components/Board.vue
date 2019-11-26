<template>
    <div>
        <v-row class="adversory" no-gutters>
            <v-col cols="3">
                <v-row class="big_row">
                    <PlayerCard :player="adversary"></PlayerCard>
                </v-row>
                <v-row class="big_row" align-content="center" justify="center">
                    <v-btn @click="pass_turn" :disabled="!turn" x-large color="white">Pass</v-btn>
                </v-row>
                <v-row class="big_row">
                    <PlayerCard :player="player"></PlayerCard>
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
                     :selected="selected_card"
                     v-on:card_click="handle_card_click"
                     v-on:row_click="handle_row_click">
                </Row>
                <Row :cards="adversary_board['distance'].cards" :number="4"
                     :selected="selected_card"
                     v-on:card_click="handle_card_click"
                     v-on:row_click="handle_row_click">
                </Row>
                <Row :cards="adversary_board['melee'].cards" :number="3"
                     :selected="selected_card"
                     v-on:card_click="handle_card_click"
                     v-on:row_click="handle_row_click">
                </Row>
                <Row :cards="board['melee'].cards" :number="0" v-on:row_click="handle_row_click"
                     :selected="selected_card"
                     v-on:card_click="handle_card_click">
                </Row>
                <Row :cards="board['distance'].cards" :number="1"
                     :selected="selected_card"
                     v-on:card_click="handle_card_click"
                     v-on:row_click="handle_row_click">
                </Row>
                <Row :cards="board['siege'].cards" :number="2" v-on:row_click="handle_row_click"
                     :selected="selected_card"
                     v-on:card_click="handle_card_click">
                </Row>
            </v-col>
            <Row :cards="hand" :number="6" v-on:card_click="select_card" hand="true"
                 :selected="selected_card" :disabled="!turn">
            </Row>
        </v-row>

        <MulliganDialog :cards="hand"></MulliganDialog>

        <MedicDialog :cards="cemetery" :active="medic" :ids="medic_ids"
                     v-on:card_click="choose_medic_target"></MedicDialog>

        <v-dialog v-model="finished" persistent>
            <v-layout column class="full-height" style="background-color: #3F3632; padding: 15px;">
                <v-row justify="center" style="margin-bottom: 15px; color: white; font-size: 25px">
                    Your opponent left the game !
                </v-row>
                <v-row justify="center" style="margin-bottom: 15px;">
                    <iframe src="https://giphy.com/embed/K3RxMSrERT8iI" width="287" height="480" frameBorder="0" style="pointer-events: none;" v-if="won"></iframe>
                    <iframe src="https://giphy.com/embed/1xVfByxByNvUiclzzL" width="480" height="480" frameBorder="0" style="pointer-events: none;" v-else></iframe>
                </v-row>
                <v-btn style="background-color: #05DC95" @click="goToHomepage">
                    Back to homepage
                </v-btn>
            </v-layout>
        </v-dialog>
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
                    name: '',
                    faction: '',
                    lives: 2
                },
                adversary: {
                    name: '',
                    faction: '',
                    lives: 2
                },
                finished: false,
                won: true,
                adversary_left: false,
            }
        },
        beforeCreate() {
            this.$sockets.game.on('hand', (data) => {
                this.hand = data['hand'];
            });

            this.$sockets.game.on('finished', (data) => {
                this.finished = true;
                this.won = data['result']
            });

            this.$sockets.game.on('done_mulligan', (data) => {
                this.hand = data['hand'];
            });

            this.$sockets.game.on('board', (data) => {
                this.hand = data['hand'];
                this.board = data['board'];
                this.adversary_board = data['adversary_board'];
                this.cemetery = data['cemetery'];
                this.turn = data['turn'];
                this.player = data['player'];
                this.player['score'] = this.board['melee']['score'] + this.board['distance']['score'] + this.board['siege']['score']
                this.adversary = data['adversary'];
                this.adversary['score'] = this.adversary_board['melee']['score'] + this.adversary_board['distance']['score'] + this.adversary_board['siege']['score']
                this.selected_card = null;
            });

            this.$sockets.game.on('adversary disconnected', (data) => {
                this.adversary_left = true;
                this.finished = true;
                this.won = true;
            });

            this.$sockets.game.emit('get_cards');
        },
        methods: {
            select_card(data) {
                this.selected_card = data['card'];
            },
            handle_row_click(row_number) {
                if (this.selected_card) {
                    const placement = this.selected_card['placement'];
                    if (this.selected_card != null && placement['rows'].includes(row_number)) {
                        if (placement['targets'] == null) {
                            this.$sockets.game.emit('play_card', {
                                card: this.selected_card['id'],
                                target: {row: row_number, target: null}
                            });
                        } else if (placement['targets']['target_type'] == 'medic') {
                            if (placement['targets']['target_ids'].length > 0) {
                                this.medic_ids = placement['targets']['target_ids'];
                                this.medic = true;
                            } else {
                                this.$sockets.game.emit('play_card', {
                                    card: this.selected_card['id'],
                                    target: {row: row_number, target: null}
                                });
                            }
                        }
                    } else {
                        console.log('Wrong row selected');
                    }
                }
            },
            handle_card_click(data) {
                const targets = this.selected_card['placement']['targets']
                if (targets != null && targets['target_type'] == 'decoy') {
                    if (targets['target_ids'].includes(data['card']['id'])) {
                        this.$sockets.game.emit('play_card', {
                            card: this.selected_card['id'],
                            target: {row: data['row_number'], target_id: data['card']['id']}
                        });
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
                this.medic = false;
                this.medic_ids = [];
            },
            pass_turn() {
                this.$sockets.game.emit('pass')
            },
            goToHomepage(){
                this.$router.push('/');
            }
        }
    }
</script>

<style scoped>
    .score {
        height: 125px;
        text-align: center;
    }

    .big_row {
        height: 253px;
        margin-top: 3px;
    }
</style>
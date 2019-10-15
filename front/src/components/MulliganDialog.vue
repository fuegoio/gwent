<template>
    <v-dialog v-model="active" persistent>
        <v-layout column class="full-height" style="background-color: #3F3632">
            <v-progress-linear color="#3F3632" background-color="#05DC95"
                               v-model="mulligan_chronometer"></v-progress-linear>
            <p style="color: #05DC95; text-align: center; margin-top: 10px">
                Choose a card to redraw ({{mulligan_count}}/2)
            </p>

            <div style="border-radius: 14px">
                <v-col cols="12" class="description_row">
                    <v-row justify="center">
                        <v-card v-for="card in cards" style="background-color: #3F3632" @click="do_mulligan(card)"
                                :disabled="disable_mulligan" :key="card.id">
                            <v-img id="card" :src="'./cards/' + card['img_name'] + '.png'"></v-img>
                        </v-card>
                    </v-row>
                </v-col>
            </div>

            <v-btn :disabled="disable_mulligan" class="skip-button" style="background-color: #05DC95"
                   @click="skip_mulligan">Skip
            </v-btn>
        </v-layout>
    </v-dialog>
</template>

<script>
    export default {
        name: "MulliganDialog",
        data() {
            return {
                active: false,
                disable_mulligan: false,
                mulligan_count: 0,
                mulligan_chronometer: 0
            }
        },
        props: ['cards'],
        methods: {
            do_mulligan(card) {
                if (this.mulligan_count < 2) {
                    this.$sockets.game.emit('mulligan', {id: card.id})
                }
            },
            skip_mulligan() {
                this.active = false;
                this.$sockets.game.emit('ready_to_play');
            },
            increment_chronometer() {
                if (this.mulligan_chronometer < 100) {
                    this.mulligan_chronometer += 0.5
                    setTimeout(() => {
                        this.increment_chronometer()
                    }, 100)
                } else if (this.active) {
                    this.active = false
                    this.$sockets.game.emit('ready_to_play');
                }
            },
        },
        beforeCreate() {
            this.$sockets.game.on('hand', (data) => {
                this.active = true
                this.increment_chronometer()
            });

            this.$sockets.game.on('done_mulligan', (data) => {
                this.mulligan_count += 1;
                if (this.mulligan_count >= 2) {
                    this.disable_mulligan = true
                    setTimeout(() => {
                        this.active = false
                        this.$sockets.game.emit('ready_to_play')
                    }, 1000);
                }
            })
        },
    }
</script>

<style scoped>
    #card {
        max-height: 300px;
        max-width: 150px;
    }

    .description_row {
        height: 300px;
    }

    .skip-button {
        margin: 20px;
        color: white;
    }
</style>
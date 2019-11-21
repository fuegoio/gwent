<template>
    <div class='board-row' @click="row_click">
        <card-transition group tag="div"
                         :class="{'row justify-center custom_row': true, 'not-highlighted': !highlight}">
            <v-card v-for="card in cards" :key="card.id"
                    :disabled="disabled" @click="card_click(card)" class="mx-1 elevation-2 board-card">
                <div class="card-overlay"></div>
                <figure class="card">
                    <v-btn v-if="!hand && card['unit_card'] && !card['hero']"
                           class="effective_power"
                           absolute
                           fab
                    >
                        {{card['effective_power']}}
                    </v-btn>
                    <v-img :src="'./cards/' + card['img_name'] + '.png'"></v-img>
                </figure>
            </v-card>
        </card-transition>
    </div>
</template>

<script>
    import {createSimpleTransition} from 'vuetify/es5/util/helpers'

    const myTransition = createSimpleTransition('card-transition');

    export default {
        name: "Row",
        components: {'card-transition': myTransition},
        props: ['cards', 'disabled', 'number', 'hand', 'selected'],
        computed: {
            highlight() {
                if (!this.hand && this.selected !== null) {
                    return this.selected.placement.rows.indexOf(this.number) > -1;
                }
                return true;
            }
        },
        methods: {
            row_click() {
                this.$emit('row_click', this.number)
            },
            card_click(card) {
                this.$emit('card_click', {card: card, row_number: this.number});
            }
        }
    }
</script>

<style scoped>
    .board-row {
        width: 100%;
    }

    .board-card {
        border-radius: 14px;
    }

    .card {
        width: 90px;
        height: 116px;
        overflow: hidden;
        margin: 0;
        border-radius: 12px;
    }

    .card-overlay {
        height: 100%;
        width: 100%;
        position: absolute;
        background-color: #05DC95;
        border-radius: 14px;
        opacity: 0;
        transition: 0.6s cubic-bezier(0.25, 0.8, 0.5, 1);
    }

    .custom_row {
        height: 125px;
        padding: 2px;
        margin-top: 3px;
        border: solid #05DC95;
        border-radius: 14px;
    }

    .not-highlighted {
        border: solid #dc6072;
    }

    .effective_power {
        width: 25px;
        height: 25px;
    }

    .card-transition-enter-active, .card-transition-leave-active {
        transition: 0.3s cubic-bezier(0.25, 0.8, 0.5, 1);
    }

    .card-transition-enter, .card-transition-leave-to {
        opacity: 0 !important;
    }

    .card-transition-move {
        transition: transform .6s;
    }

    .card-transition-enter-active .card-overlay {
        opacity: 1;
    }
</style>

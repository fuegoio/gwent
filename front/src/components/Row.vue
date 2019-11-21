<template>
    <div class='board-row' @click="row_click">
        <v-fade-transition group tag="div"
                           :class="{'row justify-center custom_row': true, 'not-highlighted': !highlight}">
            <v-card v-for="card in cards" style="border-radius: 14px;" :key="card.id"
                    :disabled="disabled" @click="card_click(card)" class="mx-1 elevation-2">
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
        </v-fade-transition>
    </div>
</template>

<script>
    export default {
        name: "Row",
        components: {},
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

    .card {
        width: 90px;
        height: 116px;
        overflow: hidden;
        margin: 0;
        border-radius: 12px;
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
</style>
<template>
    <v-row justify="center" style="margin: 0" v-if="!description" class="custom_row" @click="row_click">
        <v-card v-for="card in cards" style="background-color: #3F3632; border-radius: 14px;" :key="card.id"
                :disabled="disabled" @click="card_click(card)">
            <figure id="without_description">
                <v-btn v-if="!hand && card['unit_card'] && !card['hero']" class="effective_power"
                       absolute
                       fab
                >
                    {{card['effective_power']}}
                </v-btn>
                <v-img :src="'./cards/' + card['img_name'] + '.png'"></v-img>
            </figure>
        </v-card>
    </v-row>
</template>

<script>
    export default {
        name: "Row",
        components: {},
        props: ['cards', 'description', 'disabled', 'number', 'hand'],
        methods: {
            row_click() {
                this.$emit('row_click', this.number)
            },
            card_click(card){
                this.$emit('card_click', {card: card, row_number: this.number});
            }
        }
    }
</script>

<style scoped>
    #without_description {
        width: 90px;
        height: 125px;
        overflow: hidden;
        margin: 0;
        border-radius: 12px;
    }

    .custom_row {
        height: 125px;
        padding: 0;
        border-color: coral;
        background-color: #B78D9C;
        border-radius: 14px;
    }

    .effective_power {
        width: 25px;
        height: 25px;
    }
</style>
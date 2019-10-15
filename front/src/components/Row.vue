<template>
    <div style="background-color: #B78D9C; border-radius: 14px" @click="row_click">
        <v-col v-if="!description" cols="12" class="row">
            <v-row justify="center" style="margin: 0">
                <v-card v-for="card in cards" style="background-color: #3F3632; border-radius: 14px;"
                        :disabled="disabled" @click="card_click(card)">
                    <figure id="without_description">
                        <v-btn v-if="!hand" class="effective_power"
                            absolute
                            fab
                        >
                            {{card.effective_power}}
                        </v-btn>
                        <v-img :src="'./cards/' + card['img_name'] + '.png'"></v-img>
                    </figure>
                </v-card>
            </v-row>
        </v-col>
    </div>
</template>

<script>
    export default {
        name: "Row",
        components: {},
        props: ['cards', 'description', 'disabled', 'number', 'hand'],
        methods: {
            row_click(){
                this.$emit('row_click', this.number)
            },
            card_click(card){
                this.$emit('card_click', card);
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

    .row {
        height: 125px;
        margin: 2px;
        padding: 0;
        border-color: coral;
    }

    .effective_power {
        width: 25px;
        height: 25px;
    }
</style>
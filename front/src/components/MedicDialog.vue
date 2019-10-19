<template>
    <v-dialog v-model="active" persistent>
        <v-layout column class="full-height" style="background-color: #3F3632">
            <p style="color: #05DC95; text-align: center; margin-top: 10px">
                Choose a card to resuscitate
            </p>

            <v-col cols="12" class="description_row">
                <v-row justify="center">
                    <v-card v-for="card in cards" style="background-color: #3F3632" @click="card_click(card)"
                            :key="card.id" v-if="ids.includes(card.id)">
                        <v-img id="card" :src="'./cards/' + card['img_name'] + '.png'"></v-img>
                    </v-card>
                </v-row>
            </v-col>
        </v-layout>
    </v-dialog>
</template>

<script>
    export default {
        name: "MedicDialog",
        props: ['cards', 'active', 'ids'],
        methods: {
            card_click(card) {
                this.$emit('card_click', card);
            }
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
</style>
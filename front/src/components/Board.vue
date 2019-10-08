<template>
    <v-layout column class="full-height">
        <v-flex  v-for="row in rows" id="rows">
            <Row
                :key="row.id"
                :cards="row.cards"
            ></Row>
        </v-flex>
    </v-layout>
</template>

<script>
    import Row from "./Row"

    export default {
        name: "Board",
        components: {Row},
        data() {
            return {
                rows: [
                    {id: 1, cards: ['/cards/arachas1.png', '/cards/arachas2.png', '/cards/arachas3.png']},
                    {id: 2, cards: ['/cards/archer.png']},
                    {id: 3, cards: ['/cards/catapult.png']}
                ]
            }
        },
        mounted() {
            console.log(this.$vueSocketIo)
            this.$socket.emit('get_cards');
            this.$socket.on('deck', (data) => {
                console.log(data);
            })
        },
        sockets: {
            deck(data) {
                console.log('Poulet')
                console.log(data)
            }
        },
        methods: {

        }
    }
</script>

<style scoped>
    #rows {
        background-color: red;
        width: 95%;
        height: 30%;
        margin-top: 2.5%;
        margin-left: 2.5%;
    }

    .full-height {
        height: 100%;
    }
</style>
<template>
    <v-layout row class="full-height">
        <v-flex v-for="card in cards" class="full-height">
            <Card
                v-bind:image="card"
            ></Card>
        </v-flex>
    </v-layout>
</template>

<script>
    import Card from "./Card";
    export default {
        name: "Row",
        components: {Card},
        props: ['cards']
    }
</script>

<style scoped>
    .full-height {
        height: 100%;
    }
</style>
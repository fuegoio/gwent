<template>
    <div style="background-color: blue">
        <v-row style="background-color: red">
            <v-img :src="'./cards/' + faction_to_image[player['faction']] + '.png'"></v-img>
        </v-row>
        <v-row>
            {{player['name']}}
            {{player['faction']}}
            {{player['lives']}}
        </v-row>
    </div>
</template>

<script>
    export default {
        name: "PlayerCard",
        components: {},
        props: ['player'],
        data: () => ({
            faction_to_image: {
                northern: 'foltest_forged',
                nilfgaardian: '',
                scoiatael: 'francesca_beautiful',
                monster: 'eredin_bringer',
            }
        })
    }
</script>

<style scoped>

</style>
<template>
    <v-row>
        <v-col style="margin: 0; padding: 0">
            <figure class="card">
                <v-img v-if="player['faction']" :src="'./cards/' + faction_to_image[player['faction']] + '.png'"></v-img>
            </figure>
        </v-col>
        <v-col>
            <v-row style="margin: 0">
                <v-col style="padding: 0">
                    <v-img v-if="player['lives'] == 2" src="ruby.png" class="ruby"></v-img>
                    <v-img v-if="player['lives'] == 1" src="ruby-grey.png" class="ruby"></v-img>
                </v-col>
                <v-col style="padding: 0">
                    <v-img v-if="player['lives'] > 0" src="ruby.png" class="ruby"></v-img>
                    <v-img v-if="player['lives'] == 0" src="ruby-grey.png" class="ruby"></v-img>
                </v-col>
            </v-row>
            Username: {{player['name']}}<br>
            Faction: {{player['faction']}}<br>


        </v-col>
    </v-row>
</template>

<script>
    export default {
        name: "PlayerCard",
        components: {},
        props: ['player'],
        data: () => ({
            faction_to_image: {
                northern: 'foltest_forged',
                nilfgaardian: 'emhyr_imperial',
                scoiatael: 'francesca_beautiful',
                monster: 'eredin_bringer',
            }
        })
    }
</script>

<style scoped>
    .card {
        width: 180px;
        height: 250px;
        overflow: hidden;
        margin: 0;
        border-radius: 12px;
    }
    .ruby {
        height: 50px;
        width: 50px;
    }
</style>
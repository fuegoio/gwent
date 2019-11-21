<template>
  <v-row no-gutters>
    <v-col class="px-2">
      <figure class="card">
        <v-img
          v-if="player['faction']"
          :src="'./cards/' + faction_to_image[player['faction']] + '.png'"
          style=""
        ></v-img>
      </figure>
    </v-col>
    <v-col class="fill-height">
      <v-card :class="{'fill-height pa-3 stats': true, 'passed': player.passed}" dark>
        Username: {{ player.name }}<br />
        Faction: {{ player.faction }}<br />
        Score: {{ player.score }}<br />
        Cards in hand: {{ player.hand_length }}<br />
        <v-row align="center" class="mt-5" justify="center">
          <v-col style="padding: 0" cols="3">
            <v-img
              v-if="player['lives'] !== 0"
              src="ruby.png"
              class="ruby"
              style="margin: 0"
            ></v-img>
            <v-img v-else src="ruby-grey.png" class="ruby"></v-img>
          </v-col>
          <v-col cols="3"></v-col>
          <v-col style="padding: 0" cols="3">
            <v-img
              v-if="player['lives'] === 2"
              src="ruby.png"
              class="ruby"
            ></v-img>
            <v-img
              v-else-if="player['lives'] < 2"
              src="ruby-grey.png"
              class="ruby"
            ></v-img>
          </v-col>
        </v-row>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: "PlayerCard",
  components: {},
  props: ["player", "score"],
  data: () => ({
    faction_to_image: {
      northern: "foltest_forged",
      nilfgaardian: "emhyr_imperial",
      scoiatael: "francesca_beautiful",
      monster: "eredin_bringer"
    }
  })
};
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

.stats {
  border: solid #05dc95;
  border-radius: 14px;
}

.passed {
  border: solid #dc6072 !important;
}
</style>

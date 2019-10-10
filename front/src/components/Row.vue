<template>
    <v-col cols="12">
      <v-row justify="center">
        <v-card v-for="card in cards" style="background-color: #3F3632">
          <v-img id="card" :src="'./cards/' + card['img_name'] + '.png'"></v-img>
        </v-card>
      </v-row>
    </v-col>
</template>

<script>
    export default {
        name: "Row",
        components: {},
        props: ['cards', 'mulligan']
    }
</script>

<style scoped>
    .full-height {
        height: 100%;
    }
    #card {
        max-height: 300px;
        max-width: 150px;
        border-radius: 18px;
    }
</style>
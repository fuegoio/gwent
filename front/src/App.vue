<template>
  <v-app>
    <v-content style="height: 100%">
      <Board/>
    </v-content>
  </v-app>
</template>

<script>
  import Board from './components/Board';

  export default {
    name: 'App',
    components: {
      Board,
    },
    data: () => ({
      state: "not_connected",
      blocked: false,
    }),
    created: () => ({

    }),
    mounted: () => ({
      this.$socket.emit('emit_method', {})
    }),
    methods: {

    }
  };
</script>

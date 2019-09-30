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
    mounted(){
      this.$socket.on('connect', data => {
        console.log('[SOCKET-IO] Connected to server')
        this.$socket.emit('connected')
      })

      this.$socket.on('disconnect', data => {
        console.log('[SOCKET-IO] Disconnected to server')
        //this.$socket.emit('connected')
      })
    },
    methods: {

    }
  };
</script>

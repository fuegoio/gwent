<template>
  <v-app>
    <v-content style="height: 100%; background-color: #3F3632">
      <v-container style="height: 100%" fluid>
        <router-view :key="$route.fullPath"></router-view>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
  export default {
    name: 'App',
    data: () => ({
      state: "not_connected",
      blocked: false,
    }),
    beforeCreate() {
      this.$sockets.main.on('connect', data => {
        console.log('[SOCKET-IO] Connected to server');
        this.$sockets.main.emit('connected')
      });

      this.$sockets.main.on('disconnect', data => {
        console.log('[SOCKET-IO] Disconnected to server')
      });
    }
  };
</script>

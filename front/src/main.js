import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import VueSocketIO from 'vue-socket.io'

Vue.config.productionTip = false

Vue.use(new VueSocketIO({
    debug: true,
    connection: 'localhost:3000'
}))

new Vue({
  vuetify,
  sockets: {
    connect: function () {
      console.log('socket connected')
    },
  },
  render: h => h(App),

}).$mount('#app')



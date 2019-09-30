import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import VueSocketIO from 'vue-socket.io'
import * as io from 'socket.io-client'

Vue.config.productionTip = false

Vue.use(new VueSocketIO({
    debug: false,
    connection: 'localhost:3000'
}))
// io('http://localhost:3000')
new Vue({
  vuetify,
  render: h => h(App),

}).$mount('#app')



import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import VueSocketIO from 'vue-socket.io'
import VueRouter from 'vue-router'

import GameFinder from "./components/GameFinder";
import Board from "./components/Board";

Vue.config.productionTip = false

Vue.use(new VueSocketIO({
    debug: false,
    connection: 'http://localhost:3000/'
}))

const router = new VueRouter({
    routes: [
        {path: '/', component: GameFinder},
        {path: '/game', component: Board}
    ]
})

Vue.use(VueRouter)

new Vue({
    vuetify,
    router,
    render: h => h(App),
}).$mount('#app')


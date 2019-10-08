import Vue from 'vue';
import VueRouter from 'vue-router';

import GameFinder from "../components/GameFinder";
import Board from "../components/Board";

Vue.use(VueRouter);

export default new VueRouter({
    routes: [
        {path: '/', component: GameFinder},
        {path: '/game', component: Board}
    ]
})

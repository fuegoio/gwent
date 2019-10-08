import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from './plugins/router';
import sockets from './plugins/sockets';


Vue.config.productionTip = false;

Vue.prototype.$sockets = sockets;

new Vue({
    vuetify,
    router,
    render: h => h(App),
}).$mount('#app')


// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Vuetify from 'vuetify'
import VueResource from 'vue-resource'
import L from 'leaflet'

Vue.config.productionTip = false

Vue.use(Vuetify)
Vue.use(L)
Vue.use(VueResource)
Vue.http.options.root = "SOMESITE"
Vue.http.options.crossOrigin = true


import '../node_modules/leaflet/dist/leaflet.css';

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})

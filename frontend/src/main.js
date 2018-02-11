// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Vuetify from 'vuetify'
import VueResource from 'vue-resource'
import L from 'leaflet'
import lodash from 'lodash'
import VueLodash from 'vue-lodash'

Vue.config.productionTip = false

Vue.use(Vuetify)
Vue.use(L)
Vue.use(VueResource)
Vue.use(VueLodash, lodash)
Vue.http.options.root = "http://riverguard.ddns.net:8080/"
Vue.http.options.crossOrigin = true

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})

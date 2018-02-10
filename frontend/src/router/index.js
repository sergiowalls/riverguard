import Vue from 'vue'
import Router from 'vue-router'
import Drawer from '@/components/Drawer'
import Home from '@/components/Home'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      components: {
        drawer: Drawer,
        content: Home
      }
    }
  ]
})

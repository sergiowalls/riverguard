import Vue from 'vue'
import VueResource from 'vue-resource'

Vue.use(VueResource)

export const TestResource = () => {
  return Vue.resource('SOMEURL{/id}')
}

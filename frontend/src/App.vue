<template>
  <div id="app">
    <v-app id="fishboard">
      <v-content>
        <router-view name="drawer"/>
        <router-view name="content"/>
      </v-content>
    </v-app>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
</style>

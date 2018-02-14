<template>
  <v-app>
  <v-toolbar
    color="indigo"
    dark
    :clipped-left="$vuetify.breakpoint.mdAndUp"
    fixed
    app>
    <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
    <v-toolbar-title>RiverGuard</v-toolbar-title>
  </v-toolbar>
  </v-app>
</template>

<script>
export default {
  name: "drawer",
  data () {
    return {
      items: [
        { title: 'Home', icon: 'dashboard' },
        { title: 'About', icon: 'question_answer' }
      ],
      drawer: null
    }
  }
}
</script>

<style scoped>

</style>

<template>
  <v-card raised>
    <v-card-title primary-title>
      <span class="headline" :color="color">{{title}}</span>
    </v-card-title>
    <v-card-text>
      <v-icon :color="color" x-large>{{icon}}</v-icon>
      <span class="ml-3 title">{{content}}</span>
    </v-card-text>
  </v-card>
</template>

<script>
    export default {
        name: "k-p-i",
      props: ['title', 'icon', 'content', 'color']
    }
</script>

<style scoped>

</style>

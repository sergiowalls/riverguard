<template>
  <v-container grid-list-md fluid>
    <v-layout row>
      <v-flex xs4><k-p-i title="SOMETHING" icon="insert_comment" content="3%" color="primary"></k-p-i></v-flex>
      <v-flex xs4><k-p-i title="SOMETHING" icon="warning" content="3%" color="warning"></k-p-i></v-flex>
      <v-flex xs4><k-p-i title="SOMETHING" icon="insert_chart" content="3%" color="error"></k-p-i></v-flex>
    </v-layout>
    <v-layout row>
      <v-flex xs8>
        <div id="mapid" style="width: 100%;"></div>
      </v-flex>
      <v-flex xs4>
        <v-data-table>

        </v-data-table>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  import KPI from "./KPI";
export default {
  components: {KPI},
  name: 'home',
  data () {
      return {
        mymap: null
      }
  },
  mounted : function () {
    this.mymap = L.map('mapid').setView([36.5219,  -6.2783], 10);
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
      maxZoom: 18,
      attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
      '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
      'Imagery © <a href="http://mapbox.com">Mapbox</a>',
      id: 'mapbox.streets'
    }).addTo(this.mymap);
  }
}
</script>

<style scoped>
  #mapid {
    height: 400px;
  }
</style>

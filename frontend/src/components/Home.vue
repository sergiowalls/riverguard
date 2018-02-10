<template>
  <v-container grid-list-md fluid>
    <v-layout row>
      <v-flex xs4><k-p-i title="Tweets recorded" icon="insert_comment" content="267 in last hour" color="primary"></k-p-i></v-flex>
      <v-flex xs4><k-p-i title="New Locations" icon="warning" content="3 in last hour" color="warning"></k-p-i></v-flex>
      <v-flex xs4><k-p-i title="Increment" icon="insert_chart" content="3%" color="error"></k-p-i></v-flex>
    </v-layout>
    <v-layout row>
      <v-flex xs8>
        <div id="mapid" style="width: 100%;"></div>
      </v-flex>
      <v-flex xs4>
        <v-data-table
          :headers="headers"
          :items="items"
          class="elevation-1"
          item-key="id"
        >
          <template slot="items" slot-scope="props">
            <tr style="cursor: pointer;" @click="props.expanded = !props.expanded">
              <td>{{ props.item.name }}</td>
              <td class="text-xs-right">{{ props.item.coords }}</td>
            </tr>
          </template>
          <template slot="expand" slot-scope="props">
            <v-card flat>
              <v-card-text>{{props.item.text}}</v-card-text>
            </v-card>
          </template>
        </v-data-table>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  import KPI from "./KPI";
  import {TestResource} from '../api/TestResource'
  import LeafletHeatMap from 'leaflet-heatmap'
export default {
  components: {KPI},
  name: 'home',
  data () {
      return {
        mymap: null,
        items: [],
        headers: [
          {
            text: 'Name',
            align: 'left',
            sortable: false,
            value: 'name'
          },
          { text: 'Coords', value: 'coords' }
        ],
        markers: [],
        heat: []
      }
  },
  mounted: function () {

    this.mymap = L.map('mapid').setView([36.6621, -5.7604], 10);

    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
      maxZoom: 18,
      attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
      '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
      'Imagery © <a href="http://mapbox.com">Mapbox</a>',
      id: 'mapbox.streets'
    }).addTo(this.mymap);

    TestResource().get().then(response => {
      var x = response.body
      console.log(x.statuses)
      var json = x.statuses
      console.log(json)
      for (var key in x.statuses) {
        if (json[key].geo !== null) {
          var coords = json[key].geo.coordinates
          this.markers[key] = L.marker([coords[0], coords[1]]).addTo(this.mymap)
          this.markers[key].bindPopup(json[key].text)
          var item = {}
          item.id = key
          item.text = json[key].text
          item.coords = coords
          item.name = json[key].user.name
          this.items.push(item)
          var heatItem = [coords[0], coords[1], 1]
          this.heat.push(heatItem)
        }
      }
      console.log(this.heat)
      var heatMap = L.HeatLayer([this.heat],{radius: 25}).addTo(this.mymap)
    })

  }
}
</script>

<style scoped>
  #mapid {
    height: 400px;
  }
</style>

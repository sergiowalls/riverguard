<template>
  <v-container grid-list-md fluid>
    <v-layout row wrap>
      <v-flex xs12 md4><k-p-i title="Tweets recorded" icon="feedback" content="267 in last hour" color="primary"></k-p-i></v-flex>
      <v-flex xs12 md4><k-p-i title="New Locations" icon="warning" content="3 in last hour" color="warning"></k-p-i></v-flex>
      <v-flex xs12 md4><k-p-i title="Increment" icon="insert_chart" content="3%" color="error"></k-p-i></v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex xs12 md8>
        <div id="mapid" style="width: 100%; z-index: 0;"></div>
      </v-flex>
      <v-flex xs12 md4>
        <v-data-table
          :headers="headers"
          :items="items"
          class="elevation-1"
          item-key="id"
          :rows-per-page-items="rowsPageItems"
        >
          <template slot="items" slot-scope="props">
            <tr >
              <td style="cursor: pointer;" @click="props.expanded = !props.expanded" width="70%">{{ props.item.name }}</td>
              <td width="15%"><v-btn flat icon @click="up(props.item.id)"><v-icon color="green">new_releases</v-icon></v-btn></td>
              <td width="15%"><v-btn flat icon @click="down(props.item.id)"><v-icon color="red">delete</v-icon></v-btn></td>
            </tr>
          </template>
          <template slot="expand" slot-scope="props">
            <v-card flat>
              <v-card-text class="mb-0"><v-icon class="mr-2">insert_comment</v-icon>{{props.item.text}}</v-card-text>
              <v-card-text><v-icon class="mr-2">location_on</v-icon>{{props.item.coords}}</v-card-text>
              <v-card-text v-if="props.item.tags">Predicted tags: <br><v-icon class="mr-2">#</v-icon>{{props.item.tags}}</v-card-text>
              <v-card-media v-if="props.item.img" height="200px" :contain="true"><img :src="props.item.img" /></v-card-media>
            </v-card>
          </template>
        </v-data-table>
        <v-progress-circular v-show="!loaded" indeterminate color="primary"></v-progress-circular>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  import KPI from "./KPI";
  import {TestResource} from '../api/TestResource'
  import Twitter from 'Twitter'
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
        heat: [],
        loaded: false,
        rowsPageItems: [10, 20, 30, { text: 'All', value: -1 }]
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
      var json = x
      for (var key in json) {
        var tweet = json[key].tweet
        console.log(tweet)
        var item = {}
        if (tweet.geo !== null) {
          var coords = tweet.geo.coordinates
          this.markers[key] = L.marker([coords[0], coords[1]]).addTo(this.mymap)
          if (tweet.entities.media) {
            this.markers[key].bindPopup(tweet.text + '<br><img width="100%" src="'+tweet.entities.media[0].media_url+'"/>')
          } else {
            this.markers[key].bindPopup(tweet.text)
          }
          item.coords = coords
        }
          item.id = key
          item.text = tweet.text
          item.name = tweet.user.name
          item.userid = tweet.user.id
          item.tags = ''
          if (tweet.tags) {
            for (var key2 in tweet.tags) {
              item.tags += tweet.tags[key2].Label + ', '
            }
          }
          console.log('tags: ' + item.tags)
          this.items.push(item)
          if (tweet.entities.media) {
            item.img = tweet.entities.media[0].media_url
          }
        }
        console.log(this.markers)
        this.loaded = true
    })

  },
  methods: {
    findItemById: function (collection, id) {
      return this._.find(collection, function (i) {
        return i.id === id
      })
    },
    up: function (id) {
      this.deleteItem(id)
    },
    down: function (id) {
      this.deleteItem(id)
    },
    deleteItem: function (id) {
      console.log(this.items)
      for (var key in this.items) {
        if (this.items[key].id === id) {
          console.log('delete ' + key)
          this.items.splice(key, 1)
        }
      }
    }
  }
}
</script>

<style scoped>
  #mapid {
    height: 600px;
  }
</style>

<template>
  <div id="app">
    <div class="container-fluid">
      <div class="row">
        <vuenavbar></vuenavbar>
      </div>
      <div class="row">
        <vuesidenav @writeId="add_typhoonid"></vuesidenav>
        <vuecontentbody :selectedTyphoon="typhoonid"></vuecontentbody>
      </div>
    </div>
  </div>
</template>


<script>
import vuesidenav from './components/vue-sidenav'
import vuecontentbody from './components/vue-contentbody'
import vuenavbar from './components/vue-navbar'

export default {
  name: 'app',
  components: {
    vuesidenav,vuecontentbody,vuenavbar
  },
  props:['vue'],
  data () {
    return {
      typhoonid:'',
    }
  },
  methods: {
    add_typhoonid: function(typhoon_ids){
      this.typhoonid = typhoon_ids
      // console.log("App get " +this.typhoonid)
    }
  }
}




</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  overflow: hidden;
  height: 100%;
}
</style>
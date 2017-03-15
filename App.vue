<template>
  <div id="app">
    <div class="container-fluid">
      <div class="row">
        <vuenavbar></vuenavbar>
      </div>
      <div class="row">
        <vuesidenav></vuesidenav>
        <vuecontentbody></vuecontentbody>
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
}
</style>
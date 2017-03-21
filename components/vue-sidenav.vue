<template>
	<div id="navsidebar">
    <nav >
      <ul class="nav nav-pills nav-stacked">
        <li role="presentation">
          <span class="typhoon" v-bind:class="istyphoonselected ? selected : ''" aria-hidden="true" @click="typhoonshow"></span>
          <typhoonpanel :panelshow="ispanelshow"></typhoonpanel>
        </li>
        <li role="presentation">
          <span class="haiqu" v-bind:class="isdisasterselected ? selected : ''" aria-hidden="true" @click="diastershow"></span>
          <disasterpanel :disastershow="isdisasterbox"></disasterpanel>
        </li>
        <li role="presentation">
          <span class="jiangyu" aria-hidden="true"></span>
        </li>
      </ul>
    </nav>
	</div>
</template>

<script>
import typhoonpanel from './typhoon-panel'
import disasterpanel from './disaster-panel'


export default {
  name: 'vuesidenav',
  data () {
    return {
      ispanelshow:false,
      istyphoonselected:false,
      isdisasterbox:false,
      isdisasterselected:false,
      selected:"selected"
    }
  },
  components: {
    typhoonpanel,disasterpanel
  },
  methods: {
    typhoonshow: function(){
      this.ispanelshow = !this.ispanelshow
      this.istyphoonselected = !this.istyphoonselected
      this.isdisasterbox = false
      this.isdisasterselected = false
    },
    diastershow: function(){
      this.isdisasterbox = !this.isdisasterbox
      this.isdisasterselected = !this.isdisasterselected
      this.ispanelshow = false
      this.istyphoonselected = false
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #navsidebar {
    padding-left: 0px; 
    background-color: #323232;
    height: 100%;
    width: 70px;
    min-height: 100px;
    position: absolute;
    left: 0;
    z-index: 8;
  }

  li {
    height: 70px;
    width: 70px;
    background-color: #444;
  }

  .nav-stacked {
    border-radius: 0px;
  }


  .typhoon {
    display: inline-block;
    background-image: url('../assets/台风.png');
    width: 70px;
    height: 70px;
    background-repeat: no-repeat;
  }

  .haiqu {
    display: inline-block;
    background-image: url('../assets/灾害天气.png');
    width: 70px;
    height: 70px;
    background-repeat: no-repeat;
  }

  .jiangyu {
    display: inline-block;
    background-image: url('../assets/降水.png');
    width: 70px;
    height: 70px;
    background-repeat: no-repeat;
  }

  .selected {
    background-color: #4d94f8;
  }
</style>

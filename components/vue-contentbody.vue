<template>
	<div class="container-fluid" id="mapcontainer" @load="loadMap">
		<button @click="loadMap">clickme</button>
	</div>
</template>

<script>
	export default {
	  name: 'vuecontentbody',

	  data () {
	    return {
	    	roominfos:[]
	    }
	  },
	  methods: {
	  	loadMap:function(){
	  		console.log("loading map")
	  		leafletMap()
	  	},
	  }
	}

	function leafletMap(){
		var map = L.map('mapcontainer').setView([51.505, -0.09], 13);

		L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
		    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
		}).addTo(map);

		L.marker([51.5, -0.09]).addTo(map)
		    .bindPopup('A pretty CSS3 popup.<br> Easily customizable.')
		    .openPopup();
	}

	
</script>

<style>
	#mapcontainer {
		padding: 0px;
		margin-left: 70px;
		height: 100%;
		width: 100%;
		min-height: 670px;
		background-color: black;
		position: absolute;
		z-index: 1;
	}
</style>
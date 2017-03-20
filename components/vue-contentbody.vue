<template>
	<div class="container-fluid" id="map">
	</div>
</template>

<script>
	export default {
	  name: 'vuecontentbody',

	  data () {
	    return {
	    }
	  },
	  methods: {
	  },
	  computed: {
	  	loadingMap: function(){
	  		this.map = 'maocontainer'
	  		return this.map
	  	}
	  },
	  mounted: function leafletMap(){
		var map = L.map('map').setView([51.505, -0.09], 13);

		L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
		    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
		}).addTo(map);

		L.marker([51.5, -0.09]).addTo(map)
		    .bindPopup('A pretty CSS3 popup.<br> Easily customizable.')
		    .openPopup();
	  }
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

	#map {
		padding: 0px;
		margin-left: 70px;
		margin-left: 70px;
		height: 100%;
		width: 100%;
		min-height: 670px;
		z-index: 1;
	}
</style>
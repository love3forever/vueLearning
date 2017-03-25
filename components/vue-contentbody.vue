<template>
	<div class="container-fluid" id="map">
	</div>
</template>

<script>
	export default {
	  name: 'vuecontentbody',
	  data () {
	    return {
	    	leaflet:'',
	    	typhoonid:this.selectedTyphoon
	    }
	  },
	  props:['selectedTyphoon'],
	  methods: {
	  	get_typhoon_info:function(typhoon_id){
	  		var pos_url = "http://localhost:44444/apis/typhoonloc/"+typhoon_id
	  		var pos_info = []
	  		this.$http.get(pos_url).then(year_response=>{
	  		  pos_info = year_response.body['positions']
	  		  console.log(pos_info)
	  		  var latlngs = [];
	  		  for (var i = 0; i < pos_info.length; i++) {	  		  	
	  		  	let cors1 = pos_info[i].position.coordinates	  		
	  		  	let position1 = [cors1[1],cors1[0]]
	  		  	latlngs.push(position1)
	  		  	L.circleMarker(position1, {className:'leaflet-clickable',radius:4 ,fillRule:'evenodd',color: '#FDB700',stroke:true,weight:1,lineCap:"round",lineJoin:"round",fill:'#FDB700',fillOpacity:1}).addTo(this.leaflet);
	  		  }
	  		  L.polyline(latlngs, {color: 'red',stroke:true,weight:2}).addTo(this.leaflet);
	  		})
	  	}
	  },
	  watch: {
	  	selectedTyphoon: function(o,n){
	  		console.log("selectedid " +n)
	  		if (n) {
	  			this.get_typhoon_info(n)
	  		}
	  	}
	  },
	  computed: {
	  	loadingMap: function(){
	  		this.map = 'maocontainer'
	  		return this.map
	  	}
	  },
	  mounted: function leafletMap(){
		var map = L.map('map').setView([24, 133], 5)
		this.leaflet = map
		L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
		    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
		}).addTo(map)

		L.marker([24, 133]).addTo(map)
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
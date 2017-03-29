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
	    	typhoonid:this.selectedTyphoon,
	    	typhoonsLayers:{},
	    }
	  },
	  props:['selectedTyphoon'],
	  methods: {
	  	get_typhoon_info:function(typhoon_id){
	  		if (typhoon_id.length!=0) {
	  			for (var i = 0; i < typhoon_id.length; i++) {	  				
	  				
	  			}
	  		}	  		
	  	},
	  	addLayer:function(typhoon_id,target_layers){
	  		var pos_url = "http://localhost:44444/apis/typhoonloc/"+typhoon_id
	  		typhoon_id = typhoon_id.toString()
	  		var pos_info = []
	  		this.$http.get(pos_url).then(year_response=>{
	  		  pos_info = year_response.body['positions']
	  		  // console.log(pos_info)
	  		  var latlngs = []
	  		  var points = []
	  		  for (var i = 0; i < pos_info.length; i++) {	  		  	
	  		  	let cors1 = pos_info[i].position.coordinates	  		
	  		  	let position1 = [cors1[1],cors1[0]]
	  		  	latlngs.push(position1)
	  		  	var p = L.circleMarker(position1, {className:'leaflet-clickable',radius:4 ,fillRule:'evenodd',color: '#FDB700',stroke:true,weight:1,lineCap:"round",lineJoin:"round",fill:'#FDB700',fillOpacity:1}).addTo(this.leaflet)
	  		  	points.push(p)
	  		  }
	  		  var layer = L.polyline(latlngs, {color: 'red',stroke:true,weight:2}).addTo(this.leaflet)
	  		  target_layers[typhoon_id] = {}
  		  	  target_layers[typhoon_id]["line"] = layer
  		  	  target_layers[typhoon_id]["point"] = points
	  		})
	  	},
	  	removeLayer:function(typhoon_id,target_layers){
	  		let target_layer = target_layers[typhoon_id]["line"]
	  		let target_points = target_layers[typhoon_id]["point"]
	  		target_layer.remove()
	  		for (var i = 0; i < target_points.length; i++) {
	  			target_points[i].remove()
	  		}
	  		delete target_layers[typhoon_id]
	  	},
	  	addList:function(ids,targetids){
	  		return ids.filter(function(tid){
	  			return !(tid in targetids)
	  		})
	  	},
	  	removeList:function(ids,targetids){
	  		let current_ids = Object.keys(targetids)
	  		console.log("layers: "+current_ids)
	  		console.log("selection: "+ids)
	  		return current_ids.filter(function(cid){
	  			console.log(cid+" " + ids.indexOf(cid))
	  			return ids.indexOf(parseInt(cid)) == -1
	  		})
	  	}
	  },
	  watch: {
	  	selectedTyphoon: function(o,n){
	  		console.log(this.typhoonsLayers)
	  		let mid_param = this.typhoonsLayers
	  		let add_list = this.addList(this.selectedTyphoon,mid_param)
	  		let remove_list = this.removeList(this.selectedTyphoon,mid_param)
	  		console.log('add typhoond: '+add_list)
	  		console.log('remove typhoond: '+remove_list)
	  		for (var i = 0; i < add_list.length; i++) {
	  			this.addLayer(add_list[i],this.typhoonsLayers)
	  		}
	  		for (var i = 0; i < remove_list.length; i++) {
	  			this.removeLayer(remove_list[i],this.typhoonsLayers)
	  		}
	  		// this.get_typhoon_info(this.selectedTyphoon)
	  	}
	  },
	  computed: {
	  	loadingMap: function(){
	  		this.map = 'maocontainer'
	  		return this.map
	  	}
	  },
	  mounted: function leafletMap(){
		var map = L.map('map',{renderer: L.canvas()}).setView([24, 133], 5)
		this.leaflet = map
		this.typhoonsLayers = {}
		console.log("this.typhoonsLayers: "+Object.keys(this.typhoonsLayers))
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
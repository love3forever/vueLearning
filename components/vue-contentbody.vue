<template>
<!-- 	<div class="col-md-10" id="bodycontent">
		<h1>{{getData}}</h1>
		<div class="row">
		  <div class="col-sm-6 col-md-4" v-for="roominfo in roominfos">
		    <div class="thumbnail">
		      <img :src="roominfo.img">
		      <div class="caption">
		        <p></p>
		        <p><a href="#" class="btn btn-primary" role="button" :text="roominfo.anchor"></a> <a href="#" class="btn btn-default" role="button">Button</a></p>
		      </div>
		    </div>
		  </div>
		</div>
	</div> -->
</template>

<script>
	export default {
	  name: 'vuecontentbody',

	  data () {
	    return {
	    	roominfos:[]
	    }
	  },
	  computed: {
	  	getData: function (){
  			this.$http.get('http://localhost:5000/apis/douyu/roominfos').then(function(response){
  				// 响应成功回调
  				console.log(response.body)
  				return this.roominfos = response.body.roominfos
  			});
  		}
	  }
	}
</script>

<style>
	#bodycontent {
		  background: #F7F6F2;
	}
</style>
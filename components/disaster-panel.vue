<template>
	<div id="disasterbox"  v-bind:class="disastershow ? doshow : notshow">
		<div class="row">
			<div class="input-group" id="disastercheckbox">
				<label v-for="value in checkbox">
					<input type="checkbox" value="">
					{{value}}
				</label>
		    </div>
		</div>
		<div class="row">
			<div class="input-group" id="disasterradios">
				<label v-for="value in radios">
					<input type="radio" name="options" id="option1">{{value}}小时
				</label>
		    </div>
		</div>
	</div>
</template>

<script>
	export default {
	  name: 'disasterpanel',
	  props:['disastershow'],
	  data () {
	    return {
	    	checkbox:["内陆","沿岸","近海","远海"],
	    	radios:["24","48","72"],
	    	notshow:"notshow",
	    	doshow:"doshow"
	    }
	  },
	}
</script>

<style scoped>
	.notshow {
	  display: none;
	}

	.doshow {
	  display: block;
	}

	#disasterbox {
	  position: absolute;
	  width: 280px;
	  top: 0;
	  left: 70px;
	  height: 100%;
	  min-height: 70px;
	  background-color: #eee;
	}

	.row {
		margin-top: 7px;
		margin-bottom: 7px;
		margin-left: 0px;
	}

	#disastercheckbox > label {
		margin-left: 7px;
		margin-right: 7px;
	}
	#disasterradios > label {
		margin-left: 10px;
		margin-right: 10px;
	}
</style>
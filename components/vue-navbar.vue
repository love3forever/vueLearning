<template>
	<div class="container-fluid">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" id="brand-img" href="#"></a>
    </div>
	</div>
</template>

<script>
export default {
  name: 'vuenavbar',
  data () {
    return {
      
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #brand-img {
    display: inline-block;
    background-image: url('../assets/logo.png');
    width: 180px;
    height: 55px;
    background-repeat: no-repeat;
    margin-top: 5px;
  }
</style>

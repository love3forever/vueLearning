<template>
	<div id="typhoonpanel" v-bind:class="panelshow ? doshow : notshow">
    <div class="panel panel-default" id="year-panel">
      <div class="panel-heading">台风列表
        <div class="btn-group" id="year-btn">
          <button id="selector-btn" class="btn btn-default btn-xs dropdown-toggle" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            2016 <span class="caret"></span>
          </button>
          <ul class="dropdown-menu" id="year-list">
            <li v-for="year in yearlist">
              {{2017-year}}
            </li>
          </ul>
        </div>
        <span id="panel-closer">x</span>
      </div>
      <div class="panel-body" id="year-panel-body">
          <ul class="typhoon_list">
            <li v-for="year in yearlist">
              <div class="checkbox">
                <label>
                  <input type="checkbox" value="">
                  {{2017-year}}
                </label>
              </div>
            </li>
          </ul>
      </div>
    </div>
    <div class="panel panel-default" id="info-panel">
        <div class="panel-heading">
          路径信息
        </div>
        <div class="panel-body" id="info-panel-body">
          <table class="table" id="info-table">
                <thead>
                  <tr>
                    <th>#</th>
                    <th>时间</th>
                    <th>风向</th>
                    <th>风速</th>
                    <th>强度</th>
                  </tr>
                </thead>
                <tbody>
                  <tr class="info" v-for="year in yearlist">
                    <th scope="row">{{year}}</th>
                    <td>{{year+1}}</td>
                    <td>风向</td>
                    <td>风俗</td>
                    <td>强度</td>
                  </tr>
                </tbody>
              </table>
        </div>
    </div>
	</div>

</template>

<script>
export default {
  name: 'typhoonpanel',
  props: ['panelshow'],
  data () {
    return {
      yearlist:[1,2,3,4,5,6,7,8],
      notshow:"notshow",
      doshow:"doshow"
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .notshow {
    display: none;
  }

  .doshow {
    display: block;
  }


  #typhoonpanel {
    position: absolute;
    width: 300px;
    top: 0;
    left: 70px;
    height: 100%;
    min-height: 640px;
  }
  
  #year-panel {
    height: 50%;
    margin-bottom: 0px;
  }

  #year-panel-body {
    padding: 0px;
    margin-bottom: 0px;
  }


  .panel-heading {
    text-align: left;
    padding-top: 18px;
  }

  .typhoon_list {
    overflow: hidden;
    width: auto;
    height: 274px;
    padding: 0px;
    text-align: left;
    max-height: 270px;
    overflow: auto;
  }

  .typhoon_list > li {
    position: relative;
    padding: 6px 8px;
    border-bottom: 1px dashed #e5e5e5;
    line-height: 24px;
    width: 299px;
    height: 37px;
  }

  .typhoon_list > li > checkbox {
      margin-top: 0px;
  }

  #year-btn {
    margin-left: 10px;
  }

  #year-list {
    max-height: 312px;
    overflow: auto;
    z-index: 2;
    width: 105px;

  }

  #selector-btn{
    width: 140px;
  }

  #panel-closer {
    float: right;
  }

  #year-list > li {
    height: 25px;
  }

  #info-panel {
    padding: 0px;
    margin-bottom: 0px;
  }

  #info-panel-body {
    padding: 0px;
  }

  #info-table {
    max-height: 270px;
    margin-bottom: 0px;
  }
</style>

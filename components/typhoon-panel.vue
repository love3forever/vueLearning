<template>
	<div id="typhoonpanel" v-bind:class="panelshow ? doshow : notshow">
    <div class="panel panel-default" id="year-panel">
      <div class="panel-heading">{{typhoons}}
        <div class="btn-group" id="year-btn">
          <select id="year-list" @change="changeYear"> 
            <option v-for="year in yearlist">{{year}}</option> 
          </select>
        </div>
        <span id="panel-closer">x</span>
      </div>
      <div class="panel-body" id="year-panel-body">
          <ul class="typhoon_list">
            <li v-for="typhoon in typhoon_by_year">
              <div class="checkbox">
                <label>
                  <input type="checkbox" :value="typhoon.typhoonid" v-model="selectedids">
                  {{typhoon.seqnum}} {{typhoon.cnname}} {{typhoon.enname}}
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
          <div id="table-title">
            <span class="s1">时间</span>
            <span class="s2">风速</span>
            <span class="s3">风向</span>
            <span class="s4">强度</span>
          </div>
          </thead>
          <div id="body-container">
            <table id="info-table">
              <tbody  id="info-body">
                <tr class="info" v-for="info in typhooninfos">
                  <td class="t1">{{info.pasttimestr}}</td>
                  <td class="t2">{{info.movedir}}</td>
                  <td class="t3">{{info.topspeed}}</td>
                  <td class="t4">{{info.class}}</td>
                </tr>
              </tbody>
            </table>
          </div>  
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
      doshow:"doshow",
      typhoon_by_year:[],
      typhooninfos:[],
      selectedids:[],
    }
  },
  methods: {
    gettyphoons: function(){
      this.$http.get('http://localhost:44444/apis/typhoon/1949').then(response => {
        console.log(response.body)
        this.$http.get('')
      });
    },
    changeYear: function(){
      var selected = event.target;
      var text = $(selected).find('option:selected').text()
      console.log("载入"+text+"年信息")
      this.get_typhoon_by_year(text)
    },
    get_typhoon_by_year: function(year){
      var current_year = 'http://localhost:44444/apis/typhoon/'+year
      this.$http.get(current_year).then(year_response=>{
        this.typhoon_by_year = year_response.body['typhoon']
      })
    },
    get_info_by_id: function(typhoon_id){    
      var current_id = 'http://localhost:44444/apis/typhooninfo/'+typhoon_id
      this.$http.get(current_id).then(id_response=>{
        this.typhooninfos = id_response.body['typhooninfo']
        // console.log(this.typhooninfos)
        this.$emit('get_info_by_id',this.selectedids)     
      })
    },
    selectYear: function(selected_year){
      this.get_info_by_id(selected_year)
    }
  },
  computed: {
    typhoons : function() {
      // body...
      this.$http.get('http://localhost:44444/apis/typhooninfo/years').then(response => {

          // get body data
          this.yearlist = response.body['years']
          this.get_typhoon_by_year(this.yearlist[0])
        });
      return '台风信息'
    }
  },
  watch: {
    selectedids: function(o,n){
      // console.log(n)
      // console.log(this.selectedids)
      let ids = this.selectedids.length
      // console.log(ids)
      if (ids!=0) {
        this.get_info_by_id(this.selectedids[ids-1])
      }
      else {
        // console.log('nothing')
        this.typhooninfos = []
        this.$emit('get_info_by_id',this.selectedids)
      }
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

  .panel-body {
    overflow: hidden;
  }

  .typhoon_list {
    width: auto;
    height: 100%;
    padding: 0px;
    text-align: left;
    overflow-y: auto;
    overflow-x: hidden;
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
    overflow: hidden;
    position: relative;
    display: block;
  }

  #info-table {
    max-height: 270px;
    margin-bottom: 0px;
  }

  #table-title > span {
    display:inline-block;
    height:30px;
    line-height:30px;
    text-align:center;
    font-weight:bold;
    color:#4d94f8;
  }

  .s1 {
    width: 83px;
  }

  .s2 {
    width: 50px;
  }

  .s3 {
    width: 49px;
  }

  .s4 {
    width: 69px;
  }

  .t1 {
    width: 95px;
  }

  .t2 {
    width: 60px;
  }

  .t3 {
    width: 59px;
  }

  .t4 {
    width: 67px;
  }

  #body-container {
    overflow: auto;
    display: block;
    height: 270px;  
  }

  #info-body {
    overflow: auto;
  }

  .info > td {
    text-align: center;
    font-family: 微软雅黑;
    font-size: small;
  }
</style>

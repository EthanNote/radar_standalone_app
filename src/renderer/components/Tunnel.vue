<template>
  <div>
    <div>
      <canvas id="distance_chart" width="1920" height="900" class="animated pulse"></canvas>
    </div>
    <h1 class="current_distance">当前距离： {{ measures[measures.length-1].distance }}m</h1>
    <el-button @click="updateChart">update</el-button>
    <el-button @click="pushNewValue('1.7', 1500)">test</el-button>
  </div>
</template>

<script>
import Chart from 'chart.js'

export default {
  data () {
    return {
      measures: [
        {time: '2019.1.1', distance: 0},
        {time: '2019.1.2', distance: 1},
        {time: '2019.1.3', distance: 100},
        {time: '2019.1.4', distance: 500},
        {time: '2019.1.5', distance: 1200}
      ]
    }
  },
  mounted () {
    var ctx2 = document.getElementById('distance_chart')
    // var self = this
    this.chart = new Chart(ctx2, {
      type: 'bar',
      data: {
        datasets: [
          {
            label: 'data',
            backgroundColor: 'rgba(225,10,10,0.3)',
            borderColor: 'rgba(225,103,110,1)',
            borderWidth: 1,
            pointStrokeColor: '#fff',
            pointStyle: 'crossRot',
            data: [],
            cubicInterpolationMode: 'monotone',
            spanGaps: 'false',
            fill: 'false'
          }
        ]
      }
    //   data: self.plotData
    //   options: self.plotData
    })
    this.updateChart()
    window.eventBus.$on('tunnel', (arg) => {
      this.pushNewValue(arg.time, arg.distance)
    })

    // console.log(this.chart)
    // window.testchart = this.chart
    // window.testdata = this.plotData
  },
  methods: {

    updateChart () {
      var label = []
      var distance = []
      for (var i = 0; i < this.measures.length; i++) {
        label.push(this.measures[i].time)
        distance.push(this.measures[i].distance)
      }
      this.chart.data.datasets[0].data = distance
      this.chart.data.labels = label

      console.log('update')
      this.chart.update()
    },
    pushNewValue (time, distance) {
      this.measures.push({time: time, distance: distance})
      this.updateChart()
    }

  }
}
</script>


<style>
#myChart2 {
  height: 60%;
}

.current_distance {
  font-size: 24px;
  text-align: center;
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
}
</style>

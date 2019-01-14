<template>
  <div>
    <div>
      <h1>多目标统计</h1>
      <div>
        <canvas id="mutgt_dstbt" width="1920" height="900"></canvas>
      </div>
      <el-table :data="getMultargetStatics" height="250" border style="width: 100%">
        <el-table-column prop="targetcount" label="目标数" width="180"></el-table-column>
        <el-table-column prop="framecount" label="帧数" width="180"></el-table-column>
        <el-table-column prop="sourcetime" label="来源时间"></el-table-column>
      </el-table>
    </div>
    <div>
      <h1>逐帧统计</h1>
      <div>
        <canvas id="fmtgt_dstbt" width="1920" height="900"></canvas>
      </div>
      <div v-for="frame in frames" :key="frame.index">
        <h3>帧时间：{{frame.time}}</h3>
        <h5>目标数量：{{frame.targets.length}}</h5>
        <el-table :data="frame.targets" height="250" border style="width: 100%">
          <el-table-column prop="distance" label="距离" width="180"></el-table-column>
          <el-table-column prop="angle" label="角度" width="180"></el-table-column>
          <el-table-column prop="x" label="x" width="180"></el-table-column>
          <el-table-column prop="y" label="y" width="180"></el-table-column>
        </el-table>
      </div>
    </div>
  </div>
</template>


<script>
import Chart from 'chart.js'
export default {
  data () {
    return {
      frames: [
        {
          time: 'test1_1',
          targets: [{ distance: 100, angle: 10, x: 0, y: 1 }]
        },
        {
          time: 'test1_2',
          targets: [{ distance: 100, angle: 10, x: 0, y: 1 }]
        },
        {
          time: 'test1_3',
          targets: [{ distance: 100, angle: 10, x: 0, y: 1 }]
        },
        {
          time: 'test1_4',
          targets: [{ distance: 100, angle: 10, x: 0, y: 1 }]
        },
        {
          time: 'test1_5',
          targets: [{ distance: 100, angle: 10, x: 0, y: 1 }]
        },
        {
          time: 'test2_1',
          targets: [
            { distance: 100, angle: 10, x: 0, y: 1 },
            { distance: 100, angle: 20, x: 0, y: 1 }
          ]
        },
        {
          time: 'test1_6',
          targets: [{ distance: 100, angle: 10, x: 0, y: 1 }]
        },
        {
          time: 'test1_7',
          targets: [{ distance: 100, angle: 10, x: 0, y: 1 }]
        },
        {
          time: 'test1_8',
          targets: [{ distance: 100, angle: 10, x: 0, y: 1 }]
        },
        {
          time: 'test2_2',
          targets: [
            { distance: 100, angle: 10, x: 0, y: 1 },
            { distance: 100, angle: 20, x: 0, y: 1 }
          ]
        },
        {
          time: 'test2_3',
          targets: [
            { distance: 100, angle: 10, x: 0, y: 1 },
            { distance: 100, angle: 20, x: 0, y: 1 }
          ]
        },
        {
          time: 'test3_1',
          targets: [
            { distance: 100, angle: 10, x: 0, y: 1 },
            { distance: 100, angle: 20, x: 0, y: 1 },
            { distance: 100, angle: 20, x: 0, y: 1 }
          ]
        },
        {
          time: 'test2_4',
          targets: [
            { distance: 100, angle: 10, x: 0, y: 1 },
            { distance: 100, angle: 20, x: 0, y: 1 }
          ]
        },
        {
          time: 'test3_2',
          targets: [
            { distance: 100, angle: 10, x: 0, y: 1 },
            { distance: 100, angle: 20, x: 0, y: 1 },
            { distance: 100, angle: 20, x: 0, y: 1 }
          ]
        }
      ]
    }
  },

  methods: {
    updateChart () {
      var statics = {}
      // var sourcetimes = {}
      for (var i = 0; i < this.frames.length; i++) {
        var tcount = this.frames[i].targets.length
        if (typeof statics[tcount] === 'undefined') {
          statics[tcount] = 0
          // sourcetimes[tcount] = []
        }
        statics[tcount] += 1
        // sourcetimes[tcount].push(this.frames[i].time)
      }

      if (this.chart) {
        let labels = []
        let values = []
        for (let l in statics) {
          labels.push('' + l)
          values.push('' + statics[l])
          console.log(values)
          this.chart.update()
        }
        this.chart.data.labels = labels
        this.chart.data.datasets[0].data = values
      }

      if (this.chartFrames) {
        let labels = []
        let values = []
        for (let i = 0; i < this.frames.length; i++) {
          labels.push(this.frames[i].time)
          values.push(this.frames[i].targets.length)
        }
        this.chartFrames.data.labels = labels
        this.chartFrames.data.datasets[0].data = values
      }
    }
  },

  computed: {
    getMultargetStatics: function () {
      var statics = {}
      var sourcetimes = {}
      for (var i = 0; i < this.frames.length; i++) {
        var tcount = this.frames[i].targets.length
        if (typeof statics[tcount] === 'undefined') {
          statics[tcount] = 0
          sourcetimes[tcount] = []
        }
        statics[tcount] += 1
        sourcetimes[tcount].push(this.frames[i].time)
      }

      var result = []
      for (var key in statics) {
        console.log({
          targetcount: key,
          framecount: statics[key],
          statics: statics
        })

        result.push({
          targetcount: key,
          framecount: statics[key],
          sourcetime: sourcetimes[key].join(',')
        })
      }
      window.testStatics = statics
      // console.log(statics)
      // console.log(result)

      return result
      //   console.log(statics)
      //   return statics
    }
  },
  mounted () {
    var ctx = document.getElementById('mutgt_dstbt')
    this.chart = new Chart(ctx, {
      type: 'horizontalBar',
      data: {
        labels: [],
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
            fill: 'false',
            barThickness: 0.5
          }
        ]
      },
      options: { barPercentage: 1.0, scales: { xAxes: [{ ticks: { beginAtZero: true } }] } }
      //   data: self.plotData
      //   options: self.plotData
    })

    var ctx2 = document.getElementById('fmtgt_dstbt')
    this.chartFrames = new Chart(ctx2, {
      type: 'bar',
      data: {
        labels: [],
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
      },
      options: { scales: { yAxes: [{ ticks: { beginAtZero: true } }] } }
      //   data: self.plotData
      //   options: self.plotData
    })

    this.updateChart()
  }
}
</script>


<style>
</style>

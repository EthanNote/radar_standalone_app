<template>
  <div>
    <el-row :gutter="5">
      <el-col :xs="12" :sm="12" :md="12" :lg="12" :xl="12">
        <div class="grid-content bg-purple">
          <radar-plot></radar-plot>
        </div>
      </el-col>
      <el-col :xs="12" :sm="12" :md="12" :lg="12" :xl="12">
        <div class="grid-content bg-purple">
          <radar-video></radar-video>
        </div>
      </el-col>
    </el-row>
    <el-row :gutter="5">
      <el-col :span="24">
        <div class="grid-content bg-purple">
          <radar-frame-data></radar-frame-data>
        </div>
      </el-col>
    </el-row>
     <canvas id="myChart2" width="400px" height="400px"></canvas>
  </div>
</template>

<script>
import RadarPlot from './RadarMonitor/RadarPlot'
import RadarFrameData from './RadarMonitor/RadarFrameData'
import RadarVideo from './RadarMonitor/RadarVideo'
// import Chart from 'chart.js'

export default {
  name: 'radar-monitor',
  components: { RadarPlot, RadarFrameData, RadarVideo }
  //   methods: {
  //     open (link) {
  //       this.$electron.shell.openExternal(link);
  //     }
  //   }

  // mounted () {
  //   var ctx2 = document.getElementById('myChart2')

  //   this.myChart2 = new Chart(ctx2, {
  //     type: 'line',
  //     data: {
  //       labels: [
  //         'January',
  //         'February',
  //         'March',
  //         'April',
  //         'May',
  //         'June',
  //         'July',
  //         'August',
  //         'September',
  //         'October',
  //         'November',
  //         'December'
  //       ],
  //       datasets: [
  //         {
  //           label: 'test1',
  //           backgroundColor: 'rgba(225,10,10,0.3)',
  //           borderColor: 'rgba(225,103,110,1)',
  //           borderWidth: 1,
  //           pointStrokeColor: '#fff',
  //           pointStyle: 'crossRot',
  //           data: [65, 59, 0, 81, 56, 10, 40, 22, 32, 54, 10, 30],
  //           cubicInterpolationMode: 'monotone',
  //           spanGaps: 'false',
  //           fill: 'false'
  //         }
  //       ]
  //     },
  //     options: {}
  //   })

  //   console.log(this.myChart2)
  // }
}
</script>

<style>
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  /* background: #99a9bf; */
  background-color: #d3dce6
}
.bg-purple {
  background: white;
}
.bg-purple-light {
  background: white;
}
.grid-content {
  padding: 5px;
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>

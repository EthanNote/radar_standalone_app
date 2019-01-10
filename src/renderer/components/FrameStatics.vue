<template>
  <div>
      <div>
        <h1>多目标统计</h1>
         <el-table :data="getMultargetStatics" height="250" border style="width: 100%">
          <el-table-column prop="targetcount" label="目标数" width="180"></el-table-column>
          <el-table-column prop="framecount" label="帧数" width="180"></el-table-column>
          <el-table-column prop="sourcetime" label="来源时间" ></el-table-column>
        </el-table>
    </div>
    <div>
      <h1>逐帧统计</h1>
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
export default {
  data () {
    return {
      frames: [
        {
          time: 'test1',
          targets: [
            { distance: 100, angle: 10, x: 0, y: 1 }
          ]
        },
        {
          time: 'test2_1',
          targets: [
            { distance: 100, angle: 10, x: 0, y: 1 },
            { distance: 100, angle: 20, x: 0, y: 1 }
          ]
        },
        {
          time: 'test2_2',
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
        }
      ]
    }
  },
  computed: {
    getMultargetStatics: function () {
      var statics = {}
      var sourcetimes = {}
      for (var i = 0; i < this.frames.length; i++) {
        var tcount = this.frames[i].targets.length
        if (typeof (statics[tcount]) === 'undefined') {
          statics[tcount] = 0
          sourcetimes[tcount] = []
        }
        statics[tcount] += 1
        sourcetimes[tcount].push(this.frames[i].time)
      }

      var result = []
      for (var key in statics) {
        console.log({targetcount: key, framecount: statics[key], statics: statics})

        result.push({targetcount: key, framecount: statics[key], sourcetime: sourcetimes[key].join(',')})
      }
      window.testStatics = statics
      console.log(statics)
      console.log(result)
      return result
    //   console.log(statics)
    //   return statics
    }
  }

}
</script>


<style>
</style>

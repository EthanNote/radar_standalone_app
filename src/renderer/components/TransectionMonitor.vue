<template>
  <div>
    <el-row  class="background">
      <el-col :span="18">
        <div>
          <el-row v-for="(t, i) in reversedTransections" :key="t.index" :class="'act'+t.action">
            <el-col :span="6">
              <h3>位置: {{ t.area }}</h3>
            </el-col>
            <el-col :span="9" v-if="t.action == 0" class="inaction">
              <h3 v-if="i==0">{{t.area}}内部持续时间: {{ currentDuration/1000.0 }}秒</h3>
              <h3 v-else>{{t.area}}内部持续时间: {{ t.duration/1000 }}秒</h3>
            </el-col>
            <el-col :span="9" v-if="t.action == 1" class="outaction">
              <h3 v-if="i==0">{{t.area}}离开持续时间: {{ currentDuration/1000.0 }}秒</h3>
              <h3 v-else>{{t.area}}离开持续时间: {{ t.duration/1000 }}秒</h3>
            </el-col>
            <el-col :span="6">
              <h3>{{ getTime(t) }}</h3>
            </el-col> 
            <el-col :span="2">
              <h3>{{ getAction(t) }}</h3>
            </el-col>          
          </el-row>
        </div>
      </el-col>
      <el-col :span="6">
        <div>
          <h3>区外</h3>
          <h3>持续时间: {{outsideDuration/1000 }}秒</h3>
          <h3>限制时间: {{outsideAlarmTime/1000 }}秒</h3>
          <h3>警报进度</h3>
          <el-progress type="circle" :percentage="getAlarmPercentage" color="red"></el-progress>
        </div>
      </el-col>
    </el-row>
  </div>
</template>


<script>
var testDataCount = 0
function formatDate (d) {
  var D = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']
  return [
    [d.getFullYear(), D[d.getMonth() + 1] || d.getMonth() + 1, D[d.getDate()] || d.getDate()].join('-'),
    [D[d.getHours()] || d.getHours(), D[d.getMinutes()] || d.getMinutes(), D[d.getSeconds()] || d.getSeconds()].join(':')
  ].join(' ')
}
export default {
  data () {
    return {
      transections: [
        // {area: 'A1', time: 0, action: 1, duration: 0},
        // {area: 'A2', time: 0, action: 0, duration: 0},
        // {area: 'A3', time: 0, action: 1, duration: 0},
        // {area: 'A4', time: 0, action: 0, duration: 0}
      ],
      currentDuration: 0,
      outsideAlarmTime: 60000,
      lastMailSentID: 0
    }
  },

  methods: {

    getTime (t) {
      var date = new Date(t.time)
      return formatDate(date)
    },
    getAction (t) {
    //   console.log('' + t)
      // var date = new Date(t.time)
      if (t.action === 1) {
        return '离开 ▶'// `==[ ${t.time} ]==>`
      }
      if (t.action === 0) {
        return '◀ 进入'// `<==[ ${t.time} ]==`
      }
      return `[ERROR ACTION AT ${t.time} ${t.action}]`
    }

    // outsideDuration () {
    //   if (this.transections.length > 0) {
    //     if (this.transections[this.transections.length - 1].action === 1) {
    //       return this.currentDuration
    //     }
    //   }
    //   return '--:--'
    // }
  },

  computed: {
    getAlarmPercentage () {
      var rate = this.outsideDuration * 1.0 / this.outsideAlarmTime
      if (rate > 1) {
        rate = 1
        if (this.transections.length !== this.lastMailSentID) {
          window.eventBus.$emit('auto_mail', {event: '区外丢失', details: `目标离开区域${this.transections[this.transections.length - 1].area}超过规定时间`})
          this.lastMailSentID = this.transections.length
        }
      }
      return parseInt(rate * 100)
    },
    reversedTransections () {
      var result = []
      for (var i = this.transections.length - 1; i >= 0; i--) {
        result.push(this.transections[i])
      }
      //   if (result.length > 0) {
      //     result[0].time = this.currentDuration
      //   }
      return result
    },
    outsideDuration: function () {
      if (this.transections.length > 0) {
        if (this.transections[this.transections.length - 1].action === 1) {
          return this.currentDuration
        }
      }
      return 0
    },
    getAreaDuration: function (index, time) {
      //   if (index === 0) {
      //     return this.currentDuration
      //   }
      return time
    }

  },
  created () {
    var self = this
    window.pushTestData = function () {
      var time = new Date()
      var action = self.transections.length % 2
      if (self.transections.length > 0) {
        var lastDuration = time - self.transections[self.transections.length - 1].time
        self.transections[self.transections.length - 1].duration = lastDuration
      }
      self.transections.push({area: '室内' + testDataCount, time: time.getTime(), action: action, duration: self.currentDuration})
      if (action === 1) {
        testDataCount += 1
      }

      self.currentDuration = 0
    }

    window.eventBus.$on('transection', (data) => {
      var time = new Date(data.time)
      if (self.transections.length > 0) {
        var lastDuration = time - self.transections[self.transections.length - 1].time
        self.transections[self.transections.length - 1].duration = lastDuration
      }
      console.log(data.date)
      console.log(time)
      self.transections.push({area: data.area, time: time.getTime(), action: data.action, duration: self.currentDuration})
      self.currentDuration = 0
    })

    window.setInterval(() => {
      self.currentDuration += 100.0
    }, 100)
  }
}
</script>


<style>
.act0{
    background-color: #dfffdf;
    margin: 0
}

.act1{
    background-color: #ffd9d9;
    margin: 0
}
.background{
    background-color: #dfe5ff
}
</style>

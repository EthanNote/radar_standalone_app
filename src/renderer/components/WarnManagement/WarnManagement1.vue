<template>
  <div>
    <audio id="audio" src="/static/audio/130808.wav"/>
    <div class="container">
  	  <canvas class="stage" id="mystage" width="400" height="600" @mousedown="mousedown($event)" @mouseup="mouseup($event)"
       @mousemove="mousemove($event)">
      </canvas>
    </div>
    <div class="management">
      <el-button @click="edit">编辑</el-button>
      <el-button @click="store">保存</el-button>
      <el-button @click="clear">重置</el-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'warn-management1',
  data () {
    return {
      // x1: 0,
      // y1: 0,
      // targetID: '',
      Dot: {},
      isAllowEdit: false,
      isAllowDrawLine: false,
      isWarn: true,
      x: 0,
      y: 0,
      clientHeight: '',
      clientWidth: '',
      Width: '',
      Height: '',
      event: [],
      Data: [],
      startPoint: [],
      endPoint: [],
      Point1: [],
      Point2: [],
      Point3: [],
      Point4: [],
      Point5: [],
      Point6: [],
      Point7: [],
      Point8: [],
      Point9: [],
      Point10: [],
      i: true,
      a: true,
      b: true,
      c: true,
      d: true,
      e: true,
      f: true,
      g: true,
      h: true,
      j: true
    }
  },
  methods: {
    formatDate (d) {
      var D = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']
      return [
        [
          d.getFullYear(),
          D[d.getMonth() + 1] || d.getMonth() + 1,
          D[d.getDate()] || d.getDate()
        ].join('-'),
        [
          D[d.getHours()] || d.getHours(),
          D[d.getMinutes()] || d.getMinutes(),
          D[d.getSeconds()] || d.getSeconds()
        ].join(':')
      ].join(' ')
    },
    getlocation (x, y) {
      var cvs = document.getElementById('mystage')
      var bbox = cvs.getBoundingClientRect()
      return {
        x: (x - bbox.left - cvs.width / 2) * (cvs.width / bbox.width),
        y: -(y - bbox.top - cvs.height) * (cvs.height / bbox.height)
      }
    },
    mousedown (a) {
      if (this.isAllowEdit) {
        var cvs = document.getElementById('mystage')
        var ctx = cvs.getContext('2d')
        this.isAllowDrawLine = true
        var location1 = this.$options.methods.getlocation(a.clientX, a.clientY)
        this.startPoint.push(location1)
        ctx.moveTo(location1.x, location1.y)
        this.x = location1.x
        this.y = location1.y
        // console.log(this.x)
      }
    },
    mousemove (e) {
      if (this.isAllowDrawLine) {
        var cvs = document.getElementById('mystage')
        var ctx = cvs.getContext('2d')
        var location2 = this.$options.methods.getlocation(e.clientX, e.clientY)
        ctx.fillStyle = 'red'
        ctx.fillRect(this.x, this.y, location2.x - this.x, location2.y - this.y)
        ctx.stroke()
      }
    },
    mouseup (e) {
      this.isAllowDrawLine = false
      var location3 = this.$options.methods.getlocation(e.clientX, e.clientY)
      this.endPoint.push(location3)
      console.log(this.startPoint)
      console.log(this.endPoint)
    },
    edit () {
      this.isAllowEdit = true
    },
    store () {
      this.isAllowEdit = false
    },
    clear () {
      var cvs = document.getElementById('mystage')
      var ctx = cvs.getContext('2d')
      ctx.clearRect(-cvs.width / 2, 0, cvs.width, cvs.height)
    },
    warn () {
      var cvs = document.getElementById('mystage')
      var ctx = cvs.getContext('2d')
      var imgData = ctx.getImageData(this.Dot.x1 + cvs.width / 2, cvs.height - this.Dot.y1, 800, 400)
      var red = imgData.data[0]
      if (red === 255) {
        this.isWarn = true
      }
    },
    draw () {
      var cvs = document.getElementById('mystage')
      var ctx = cvs.getContext('2d')
      var Point = this.Dot
      if (Point.targetID % 10 === 1.0) {
        this.Point1.push(Point)
        ctx.fillStyle = '#D2691E'
      } else if (Point.targetID % 10 === 2.0) {
        this.Point2.push(Point)
        // ctx.moveTo(this.Point2[0].x * 50, this.Point2[0].y * 50)
        ctx.fillStyle = '#A0522D'
      } else if (Point.targetID % 10 === 3.0) {
        this.Point3.push(Point)
        ctx.stroke()
        // ctx.moveTo(this.Point3[0].x * 50, this.Point3[0].y * 50)
        ctx.fillStyle = '#C71585'
      } else if (Point.targetID % 10 === 4.0) {
        this.Point4.push(Point)
        // ctx.moveTo(this.Point4[0].x * 50, this.Point4[0].y * 50)
        ctx.fillStyle = '#0000FF'
      } else if (Point.targetID % 10 === 5.0) {
        this.Point5.push(Point)
        // ctx.moveTo(this.Point5[0].x * 50, this.Point5[0].y * 50)
        ctx.fillStyle = '#708090'
      } else if (Point.targetID % 10 === 6.0) {
        this.Point6.push(Point)
        // ctx.moveTo(this.Point6[0].x * 50, this.Point6[0].y * 50)
        ctx.fillStyle = '#00FFFF'
      } else if (Point.targetID % 10 === 7.0) {
        this.Point7.push(Point)
        // ctx.moveTo(this.Point7[0].x * 50, this.Point7[0].y * 50)
        ctx.fillStyle = '#00FF7F'
      } else if (Point.targetID % 10 === 8.0) {
        this.Point8.push(Point)
        // ctx.moveTo(this.Point8[0].x * 50, this.Point8[0].y * 50)
        ctx.fillStyle = '#FFD700'
      } else if (Point.targetID % 10 === 9.0) {
        this.Point9.push(Point)
        // ctx.moveTo(this.Point9[0].x * 50, this.Point9[0].y * 50)
        ctx.fillStyle = '#000000'
      } else if (Point.targetID % 10 === 0) {
        this.Point10.push(Point)
        // ctx.moveTo(this.Point9[0].x * 50, this.Point9[0].y * 50)
        ctx.fillStyle = '#4169E1'
      }
      ctx.fillRect(this.Dot.x * 50, this.Dot.y * 50, 5, 5)
      ctx.stroke()
      if (this.Point1[0] && this.i) {
        this.i = false
        ctx.moveTo(this.Point1[0].x * 50, this.Point1[0].y * 50)
      }
      if (this.Dot.targetID % 10 === 1.0) {
        ctx.lineTo(this.Dot.x * 50, this.Dot.y * 50)
      }
      if (this.Point2[0] && this.a) {
        this.a = false
        ctx.moveTo(this.Point2[0].x * 50, this.Point2[0].y * 50)
      }
      if (this.Dot.targetID % 10 === 2.0) {
        ctx.lineTo(this.Dot.x * 50, this.Dot.y * 50)
      }
      if (this.Point3[0] && this.b) {
        this.b = false
        ctx.moveTo(this.Point3[0].x * 50, this.Point3[0].y * 50)
      }
      if (this.Dot.targetID % 10 === 3.0) {
        ctx.lineTo(this.Dot.x * 50, this.Dot.y * 50)
      }
      if (this.Point4[0] && this.c) {
        this.c = false
        ctx.moveTo(this.Point4[0].x * 50, this.Point4[0].y * 50)
      }
      if (this.Dot.targetID % 10 === 4.0) {
        ctx.lineTo(this.Dot.x * 50, this.Dot.y * 50)
      }
      if (this.Point5[0] && this.d) {
        this.d = false
        ctx.moveTo(this.Point5[0].x * 50, this.Point5[0].y * 50)
      }
      if (this.Dot.targetID % 10 === 5.0) {
        ctx.lineTo(this.Dot.x * 50, this.Dot.y * 50)
      }
      if (this.Point6[0] && this.e) {
        this.e = false
        ctx.moveTo(this.Point6[0].x * 50, this.Point6[0].y * 50)
      }
      if (this.Dot.targetID % 10 === 6.0) {
        ctx.lineTo(this.Dot.x * 50, this.Dot.y * 50)
      }
      if (this.Point7[0] && this.f) {
        this.f = false
        ctx.moveTo(this.Point7[0].x * 50, this.Point7[0].y * 50)
      }
      if (this.Dot.targetID % 10 === 7.0) {
        ctx.lineTo(this.Dot.x * 50, this.Dot.y * 50)
      }
      if (this.Point8[0] && this.g) {
        this.g = false
        ctx.moveTo(this.Point8[0].x * 50, this.Point8[0].y * 50)
      }
      if (this.Dot.targetID % 10 === 8.0) {
        ctx.lineTo(this.Dot.x * 50, this.Dot.y * 50)
      }
      if (this.Point9[0] && this.h) {
        this.h = false
        ctx.moveTo(this.Point9[0].x * 50, this.Point9[0].y * 50)
      }
      if (this.Dot.targetID % 10 === 9.0) {
        ctx.lineTo(this.Dot.x * 50, this.Dot.y * 50)
      }
      if (this.Point10[0] && this.h) {
        this.j = false
        ctx.moveTo(this.Point10[0].x * 50, this.Point10[0].y * 50)
      }
      if (this.Dot.targetID % 10 === 0) {
        ctx.lineTo(this.Dot.x * 50, this.Dot.y * 50)
      }
      ctx.fillRect(this.Dot.x * 50, this.Dot.y * 50, 5, 5)
      ctx.stroke()
    },
    aplayAudio () {
      const audio = document.getElementById('audio')
      audio.play()
    }
  },
  mounted () {
    var cvs = document.getElementById('mystage')
    var ctx = cvs.getContext('2d')
    ctx.translate(cvs.width / 2, cvs.height)
    ctx.scale(1, -1)
    window.setInterval(() => {
      this.warn()
      this.draw()
    }, 10)
    window.eventBus.$on('dot', (arg) => {
      this.Dot = arg
    })
    this.Width = document.documentElement.clientWidth
    this.Height = document.documentElement.clientHeight
    const that = this
    window.onresize = function temp () {
      that.clientWidth = document.documentElement.clientWidth
      that.clientHeight = document.documentElement.clientHeight
      // cvs.width = 800 * (that.clientWidth / that.Width)
      // cvs.height = 400 * (that.clientHeight / that.Height)
      // console.log(that.clientWidth)
      // console.log(that.clientHeight)
      // console.log(cvs.width)
      // console.log(that.Width)
      // console.log(that.Height)
    }
  },
  watch: {
    isWarn: function () {
      if (this.isWarn) {
        var ipc = require('electron').ipcRenderer
        ipc.send('warnning')
        this.aplayAudio()
        var date = new Date()
        this.event = [this.formatDate(date), [this.Dot.x / 50, this.Dot.y / 50], '有人进入禁止区域']
        console.log(this.event)
        window.eventBus.$emit('warnning', this.event)
      }
    }
  }
}
</script>

<style>
.container {
  margin-top: 60px;
  text-align: center;
}
#mystage {
  border:1px solid black;
}
.management {
  margin-top: 10px;
  text-align: center;
  float: right;
}
</style>

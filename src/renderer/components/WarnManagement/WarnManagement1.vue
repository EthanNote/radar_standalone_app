<template>
  <div  class="animated slideInLeft">
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
    <el-alert
    v-show="isWarn"
    title="警告"
    type="error"
    description="有人进入禁止区域"
    show-icon>
    </el-alert>
  </div>
</template>

<script>
export default {
  name: 'warn-management1',
  data () {
    return {
      x1: 50,
      y1: 50,
      isAllowEdit: false,
      isAllowDrawLine: false,
      isWarn: false,
      x: 0,
      y: 0,
      clientHeight: '',
      clientWidth: '',
      Width: '',
      Height: '',
      Message: []
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
        ctx.moveTo(location1.x, location1.y)
        this.x = location1.x
        this.y = location1.y
        console.log(this.x)
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
    mouseup () {
      this.isAllowDrawLine = false
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
      var imgData = ctx.getImageData(this.x1 + 2 + cvs.width / 2, cvs.height - this.y1, 800, 400)
      var red = imgData.data[0]
      if (red === 255) {
        this.isWarn = true
      }
    },
    draw () {
      var cvs = document.getElementById('mystage')
      var ctx = cvs.getContext('2d')
      ctx.rect(this.x1, this.y1, 1, 1)
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
      this.x1 = arg.x * 50
      this.y1 = arg.y * 50
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
        this.aplayAudio()
        var date = new Date()
        this.Message = [this.formatDate(date), this.x1, '有人进入禁止区域']
        console.log(this.Message)
        window.eventBus.$emit('warnning', this.Message)
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

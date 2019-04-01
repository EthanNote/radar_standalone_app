<template>
  <div>
    <h2>警报区域设置</h2>
    <div class="pic" style="display: flex;font-size: 12px">
      <div><img  src="./img/2.png">     监控区域</div>
      <div class="img"><img  src="./img/1.png">     禁止区域</div>
    </div>
    <div class="container">
  	  <canvas class="stage" id="mystage" width="800" height="400" @mousedown="mousedown($event)" @mouseup="mouseup($event)"
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
  name: 'warn-management',
  data () {
    return {
      x1: 0,
      y1: 0,
      isAllowEdit: false,
      isAllowDrawLine: false,
      isWarn: false,
      x: 0,
      y: 0
    }
  },
  methods: {
    getlocation (x, y) {
      var cvs = document.getElementById('mystage')
      var bbox = cvs.getBoundingClientRect()
      return {
        x: (x - bbox.left) * (cvs.width / bbox.width),
        y: (y - bbox.top) * (cvs.height / bbox.height)
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
      ctx.clearRect(0, 0, 800, 400)
    },
    warn () {
      var cvs = document.getElementById('mystage')
      var ctx = cvs.getContext('2d')
      var imgData = ctx.getImageData(this.x1, this.y1, 800, 400)
      var red = imgData.data[0]
      if (red === 255) {
        this.isWarn = true
      }
    },
    draw () {
      var cvs = document.getElementById('mystage')
      var ctx = cvs.getContext('2d')
      ctx.rect(this.x1, this.y1, 2, 2)
      ctx.stroke()
    }
  },
  mounted () {
    window.setInterval(() => {
      this.warn()
      this.draw()
    }, 10)
    window.eventBus.$on('dot', (arg) => {
      this.x1 = arg.x * 50
      this.y1 = arg.y * 50
      //  console.log('message on!' + this.point)
    })
  }
}
</script>

<style>
.container {
  text-align: center;
  margin-top: 100px;
}
#mystage {
  border:1px solid black;
}
.management {
  margin-top: 10px;
  text-align: center;
  float: right;
}
.img {
  margin-left: 60px;
}
</style>

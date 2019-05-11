<template>
    <div id="radarvideo" >
        <h3>视频</h3>
        <h2 class ="rec" v-show="capture.remaining>0">● REC</h2>
        <video id="video" autoplay></video>
        <h2 class="videotime">{{ currenttime }}</h2>
        <canvas hidden id='cvs' width="480" height="320"></canvas>
    </div>
</template>

<script type="text/javascript">

var fs = require('fs')

/* eslint-disable */
var get_buffer = function () {
  var canvas = document.getElementById('cvs')
  var base64 = canvas.toDataURL('png')
  var data = base64.split('base64,')[1]
  var buf = new Buffer(data, 'base64')
  return buf
}

var video_capture = function () {
  var canvas = document.getElementById('cvs')
  var context = canvas.getContext('2d')
  var video = document.getElementById('video')

  context.drawImage(video, 0, 0, 640, 480)
}

var save_canvas_to_file = function () {
  var myDate = new Date()
  video_capture()
  var fname = './capture/' + myDate.getTime() + '.png'
  console.log('captrue frame', fname)

  var data = get_buffer()
  fs.writeFileSync(fname, data)
  return fname
}
/* eslint-enable */
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
      currenttime: '',
      capture: {
        duration: 15,
        remaining: 0,
        capturedFiles: []
      }
    }
  },
  methods: {
    captureOne () {

    }
  },

  created () {
    window.eventBus.$on('dot', (arg) => {
      this.capture.remaining = this.capture.duration * 1
    })

    // var syncHeight = function () {
    //   var height = document.getElementById('video').clientHeight
    //   console.log('RESIZE ', height)
    //   document.getElementById('plot').style.height = height + 4 + 'px'
    // }
    // window.addEventListener('resize', syncHeight)
    // window.addEventListener('load', syncHeight)
    var self = this
    window.setInterval(() => {
      var date = new Date()
      self.currenttime = formatDate(date)
      if (self.capture.remaining > 0) {
        self.capture.remaining -= 1
        // console.log(self.capture.remaining)
        video_capture()
        var fname = save_canvas_to_file()
        self.capture.capturedFiles.push(fname)
        if (self.capture.remaining <= 0) {
          // console.log('Capture finished')
          // console.log(JSON.stringify(self.capture.capturedFiles))
          self.capture.capturedFiles = []
        }
      }
    }, 200)

    var constraints = {
      audio: false,
      video: {
        width: 1280,
        height: 720
      }
    }

    navigator.mediaDevices
      .getUserMedia(constraints)
      .then(function (stream) {
        var video = document.querySelector('video')
        video.src = window.URL.createObjectURL(stream)
        video.onloadedmetadata = function (e) {
          video.play()
        }
      })
      .catch(function (err) {
        console.log(err.name + ': ' + err.message)
      })
  }

}
// window.updatePlotHeight = function () {
// var height = document.getElementById("video").clientHeight;
// console.log("RESIZE ", height);
// document.getElementById("plot").style.height = height + "px";
// }

// window.onload=func

// var promisifiedOldGUM = function (constraints) {
//   // 第一个拿到getUserMedia，如果存在
//   var getUserMedia = (navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia)

//   // 有些浏览器只是不实现它-返回一个不被拒绝的承诺与一个错误保持一致的接口
//   if (!getUserMedia) {
//     return Promise.reject(new Error('getUserMedia is not implemented in this browser-getUserMedia是不是在这个浏览器实现'))
//   }

//   // 否则，调用包在一个旧navigator.getusermedia承诺
//   return new Promise(function (resolve, reject) {
//     getUserMedia.call(navigator, constraints, resolve, reject)
//   })
// }

// 旧的浏览器可能无法实现mediadevices可言，所以我们设置一个空的对象第一
if (navigator.mediaDevices === undefined) {
  navigator.mediaDevices = {}
}

// 一些浏览器部分实现mediadevices。我们不能只指定一个对象
// 随着它将覆盖现有的性能getUserMedia。.
// 在这里，我们就要错过添加getUserMedia财产。.
// if (navigator.mediaDevices.getUserMedia === undefined) {
//   navigator.mediaDevices.getUserMedia = promisifiedOldGUM
// }
</script>

<style>
#video {
  background-color: gray;
  width: 100%;  
}



.videotime{
  color: white;
  position: relative;
  top: -50px;
  right: 5px;
  float: right;
  font-family: Arial, Helvetica, sans-serif;
  text-shadow: #000 3px 0 0, #000 0 3px 0, #000 -3px 0 0, #000 0 -3px 0;
}


.rec{
  height: 0px;
  padding: 0px;
  margin:0px;
  color: red;
  position: relative;
  top: 25px;
  left: 5px;
  float: left;
  font-family: Arial, Helvetica, sans-serif;
  text-shadow: #000 3px 0 0, #000 0 3px 0, #000 -3px 0 0, #000 0 -3px 0;
}
</style>

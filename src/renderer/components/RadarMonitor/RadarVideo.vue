<template>
    <div id="radarvideo" >
        <h3>视频</h3>
        <video id="video" autoplay>
        </video>
        <h2 class="videotime">{{ currenttime }}</h2>
    </div>
</template>

<script type="text/javascript">

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
      currenttime: ''
    }
  },
  created () {
    var syncHeight = function () {
      var height = document.getElementById('video').clientHeight
      console.log('RESIZE ', height)
      document.getElementById('plot').style.height = height + 4 + 'px'
    }
    window.addEventListener('resize', syncHeight)
    window.addEventListener('load', syncHeight)
    var self = this
    window.setInterval(() => {
      var date = new Date()
      self.currenttime = formatDate(date)
    }, 200)
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
</style>

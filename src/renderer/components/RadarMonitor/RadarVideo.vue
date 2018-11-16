<template>
    <div>
        <h3>Reference Video</h3>
        <video id="video" autoplay></video>
    </div>
</template>

<script type="text/javascript">
var constraints = {
  audio: true,
  video: {
    width: 1280,
    height: 720
  }
}

navigator.mediaDevices
  .getUserMedia(constraints)
  .then(function (stream) {
    var video = document.getElementById('video')
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
    #video{
        background-color: gray;
        width: 100%
    }
</style>

<template>
  <div>
    <el-row :gutter="5">
      <el-col :xs="24" :sm="18" :md="12" :lg="12" :xl="12">
        <div class="grid-content bg-purple">
          <svg width="640" height="480">
            <g>
              <path :d="currentdata.path"></path>
            </g>
          </svg>
        </div>
      </el-col>
      <el-col :xs="24" :sm="18" :md="12" :lg="12" :xl="12">
        <div class="grid-content bg-purple-light">
          <img :src="currentdata.image">
        </div>
      </el-col>
      <el-col :xs="24" :sm="18" :md="12" :lg="12" :xl="12">
        <div class="grid-content bg-purple"></div>
      </el-col>
      <el-col :xs="24" :sm="18" :md="12" :lg="12" :xl="12">
        <div class="grid-content bg-purple-light"></div>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="24">
        <div class="grid-content bg-transparent">
          <el-pagination background layout="prev, pager, next" :total="playbackdata.list.length" :page-size="1" v-on:current-change="setindex"></el-pagination>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
var fs = require('fs')

window.playbackdata = {
  list: [],
  index: 0
}

fs.readFile('playbacklist.json', 'utf8', function (err, data) {
  if (err) {
    console.error(err)
  } else {
    console.log(data)
    window.playbackdata.list = JSON.parse(data)
  }
})

// window.playbacktimer = window.setInterval(() => {
//   if (window.currentPlaybackData.images.length > 0) {
//     window.currentPlaybackData.index += 1;
//     if (
//       window.currentPlaybackData.index >=
//       window.currentPlaybackData.images.length
//     ) {
//       window.currentPlaybackData.index = 0;
//     }
//   }
// }, 200);

export default {
  data () {
    return {
      playbackdata: window.playbackdata,
      frameindex: 0
    }
  },

  methods: {
    setindex (index) {
      this.playbackdata.index = index - 1
    }
  },

  computed: {
    currentdata () {
      var currentplayback = null

      if (this.playbackdata.list.length > 0) {
        currentplayback = this.playbackdata.list[this.playbackdata.index]
      }

      if (currentplayback) {
        // this.playbackData.path = currentplayback.path;
        // this.playbackData.images = currentplayback.images;
        var image = ''
        if (currentplayback.images.length > 0) {
          image = currentplayback.images[this.frameindex]
        }

        return {
          path: currentplayback.path,
          image: image,
          imagelist: currentplayback.images
        }
      } else {
        return { path: '', image: '', imagelist: [] }
      }
    }

    // current_img() {
    //   var playback = this.currentdata();

    //   // this.update_list();
    //   console.log("new playback", playback);

    //   if (playback && playback.images.length > 0) {
    //     return playback.images[this.frameindex];
    //   } else {
    //     return "";
    //   }
    // },

    // current_path() {
    //   var playback = this.currentdata();
    //   if (playback) {
    //     return playback.path;
    //   } else {
    //     return "";
    //   }
    // }
  },
  created () {
    var self = this
    window.setInterval(function () {
      // self.playbacklist = window.playbacklist
      self.frameindex += 1
      if (self.frameindex >= self.currentdata.imagelist.length) {
        self.frameindex = 0
      }
    }, 1000)
  }
}
</script>



<style>
svg {
  width: 100%;
}

path {
  fill: transparent;
  stroke: rgb(0, 0, 0);
  stroke-width: 4;
  stroke-dasharray: 20;
  stroke-dashoffset: 0;
  animation: pathplayback 1s linear infinite;
}
@keyframes pathplayback {
  0% {
    stroke-dashoffset: 20;
  }

  100% {
    stroke-dashoffset: -20;
  }
}
</style>

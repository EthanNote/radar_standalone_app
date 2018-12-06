<template>
  <div>
    <el-row :gutter="5">
      <el-col :xs="24" :sm="24" :md="12" :lg="12" :xl="12">
        <div class="grid-content bg-purple">
          <div class="capture">
              <svg id="svgcontent" width="640" height="480" x="0" y="0" overflow="hidden" xmlns="http://www.w3.org/2000/svg" xmlns:se="http://svg-edit.googlecode.com" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 580 400"><!-- Created with Method Draw - http://github.com/duopixel/Method-Draw/ --><g style="pointer-events:none"><title style="pointer-events:inherit">background</title><rect x="-1" y="-1" width="582" height="402" id="canvas_background" fill="#fff" style="pointer-events:inherit"></rect><g id="canvasGrid" width="100%" height="100%" x="0" y="0" overflow="visible" display="none"><rect width="100%" height="100%" x="0" y="0" stroke-width="0" stroke="none" fill="url(#gridpattern)" style="pointer-events: none; display:visible;"></rect></g></g><g style="pointer-events:all"><title style="pointer-events:inherit">Layer 1</title><rect fill="#fff" stroke-width="15.5" x="44.500015794014416" y="30.43749243330967" width="494.9999687238001" height="342.9999772558153" id="svg_1" stroke-dasharray="none" fill-opacity="1" stroke-opacity="1" opacity="1" stroke="#323f3f"></rect><rect fill="#fff" stroke-width="0" x="21.5" y="61.4375" width="59" height="138.99999080776087" id="svg_2" stroke-dasharray="none" stroke="#323f3f"></rect><rect fill="#fff" stroke-width="1" x="68.5" y="251.43750363588333" width="141.99999906871852" height="101.00000114340801" id="svg_4" stroke-dasharray="none" stroke="#323f3f"></rect></g>
              
              <g>
                <path :d="currentdata.path"></path>
                <text
                  v-for="node in currentdata.nodes"
                  :x="node[0]"
                  :y="node[1]"
                >{{ formatDate(new Date(node[2])) }}</text>
              </g>
              </svg>
          </div>
        </div>
      </el-col>
      <el-col :xs="24" :sm="24" :md="12" :lg="12" :xl="12">
        <div class="grid-content bg-purple-light">
          <div class="capture">
            <img :src="currentdata.image">
            <h3 class="time">{{ imagedate(currentdata.image) }}</h3>
          </div>
        </div>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="24">
        <div class="grid-content bg-transparent">
          <el-pagination
            background
            layout="prev, pager, next"
            :total="playbackdata.list.length"
            :page-size="1"
            v-on:current-change="setindex"
          ></el-pagination>
        </div>
      </el-col>
    </el-row>
    <el-row>
      <el-table :data="gettable" height="250" border style="width: 100%">
        <el-table-column prop="date" label="日期" width="180"></el-table-column>
        <el-table-column prop="name" label="类型" width="180"></el-table-column>
        <el-table-column fixed="right" label="操作" width="100">
          <template slot-scope="scope">
            <el-button @click="handleClick(scope.$index)" type="text" size="small">查看</el-button>
            <el-button type="text" size="small">报警</el-button>
          </template>
        </el-table-column>
      </el-table>
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
var buildpathformnodelist = function (nodelist) {
  if (nodelist.length < 1) {
    return ''
  }

  let result = `M${nodelist[0][0]} ${nodelist[0][1]} L`

  for (let i = 1; i < nodelist.length; i++) {
    result += `${nodelist[i][0]} ${nodelist[i][1]} `
  }

  return result
}

export default {
  data () {
    return {
      playbackdata: window.playbackdata,
      frameindex: 0
    }
  },

  methods: {
    handleClick (rowindex) {
      this.playbackdata.index = rowindex
    },

    setindex (index) {
      this.playbackdata.index = index - 1
    },
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
    imagedate (url) {
      return this.formatDate(
        new Date(url.replace('./capture/', '').replace('.png', '') * 1)
      )
    }
  },

  computed: {
    gettable () {
      var result = []
      result.push({
        date: '日期',
        name: '路径'
      })
      result.push({
        date: '日期',
        name: '路径'
      })
      return result

      // return [
      //   {
      //     date: '2016-05-03',
      //     name: '王小虎',
      //     address: { x: 1 }
      //   },
      //   {
      //     date: '2016-05-03',
      //     name: '王小虎',
      //     address: { x: 1 }
      //   }
      // ]
    },

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
          path: buildpathformnodelist(currentplayback.nodes),
          nodes: currentplayback.nodes,
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
  border: gray 1px solid;
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

.time {
  color: white;
  position: relative;
  top: -50px;
  float: right;
  font-family: Arial, Helvetica, sans-serif;
  text-shadow: #000 3px 0 0, #000 0 3px 0, #000 -3px 0 0, #000 0 -3px 0;
}
.capture {
  width: 640px;
  height: 480px;
  margin: 0 auto;
}
</style>

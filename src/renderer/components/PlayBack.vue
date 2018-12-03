<template>
  <div>
    <el-row :gutter="5">
      <el-col :xs="24" :sm="18" :md="12" :lg="12" :xl="12">
        <div class="grid-content bg-purple">
          <svg width="640" height="480">
            <g>
              <path d="M 20 20 L 100 100 200 300"></path>
            </g>
          </svg>
        </div>
      </el-col>
      <el-col :xs="24" :sm="18" :md="12" :lg="12" :xl="12">
        <div class="grid-content bg-purple-light">
            <img :src="current_img"/>
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
          <el-pagination background layout="prev, pager, next" :total="1000"></el-pagination>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>

window.currentPlaybackData = {
  images: [
    './capture/1543587629511.png',
    './capture/1543587630011.png',
    './capture/1543587630512.png',
    './capture/1543587631011.png',
    './capture/1543587631512.png',
    './capture/1543587632011.png',
    './capture/1543587632511.png',
    './capture/1543587633012.png',
    './capture/1543587633510.png',
    './capture/1543587634011.png',
    './capture/1543587634511.png',
    './capture/1543587635011.png',
    './capture/1543587635511.png',
    './capture/1543587636011.png',
    './capture/1543587636510.png',
    './capture/1543587637011.png',
    './capture/1543587637511.png',
    './capture/1543587638010.png',
    './capture/1543587638511.png',
    './capture/1543587639011.png',
    './capture/1543587639512.png',
    './capture/1543587640011.png',
    './capture/1543587640512.png',
    './capture/1543587641011.png',
    './capture/1543587641511.png',
    './capture/1543587642013.png',
    './capture/1543587642511.png',
    './capture/1543587643011.png',
    './capture/1543587643511.png',
    './capture/1543587644011.png',
    './capture/1543587644511.png',
    './capture/1543587645012.png',
    './capture/1543587645512.png',
    './capture/1543587646011.png',
    './capture/1543587646512.png',
    './capture/1543587647011.png',
    './capture/1543587647511.png',
    './capture/1543587648012.png',
    './capture/1543587648510.png',
    './capture/1543587649011.png',
    './capture/1543587649512.png',
    './capture/1543587650010.png',
    './capture/1543587650511.png',
    './capture/1543587651011.png',
    './capture/1543587651511.png',
    './capture/1543587652011.png',
    './capture/1543587652512.png',
    './capture/1543587653010.png',
    './capture/1543587653511.png',
    './capture/1543587654011.png',
    './capture/1543587654512.png',
    './capture/1543587655011.png',
    './capture/1543587655512.png',
    './capture/1543587656012.png',
    './capture/1543587656511.png',
    './capture/1543587657012.png',
    './capture/1543587657512.png',
    './capture/1543587658011.png',
    './capture/1543587658511.png',
    './capture/1543587659011.png',
    './capture/1543587659510.png',
    './capture/1543587660012.png',
    './capture/1543587660511.png',
    './capture/1543587661011.png',
    './capture/1543587661511.png',
    './capture/1543587662011.png',
    './capture/1543587662511.png',
    './capture/1543587663012.png',
    './capture/1543587663511.png',
    './capture/1543587664011.png',
    './capture/1543587664512.png',
    './capture/1543587665012.png',
    './capture/1543587665510.png',
    './capture/1543587666011.png',
    './capture/1543587666511.png',
    './capture/1543587667011.png',
    './capture/1543587667511.png',
    './capture/1543587668012.png',
    './capture/1543587668511.png',
    './capture/1543587669012.png',
    './capture/1543587669512.png',
    './capture/1543587670010.png',
    './capture/1543587670511.png',
    './capture/1543587671012.png',
    './capture/1543587671510.png',
    './capture/1543587672011.png',
    './capture/1543587672512.png',
    './capture/1543587673011.png',
    './capture/1543587673511.png',
    './capture/1543587674012.png',
    './capture/1543587674512.png',
    './capture/1543587675011.png',
    './capture/1543587675513.png',
    './capture/1543587676011.png',
    './capture/1543587676512.png',
    './capture/1543587677012.png',
    './capture/1543587677511.png',
    './capture/1543587678011.png',
    './capture/1543587678512.png',
    './capture/1543587679011.png',
    './capture/1543587679511.png',
    './capture/1543587680012.png',
    './capture/1543587680510.png',
    './capture/1543587681011.png',
    './capture/1543587681512.png',
    './capture/1543587682011.png',
    './capture/1543587682511.png',
    './capture/1543587683011.png',
    './capture/1543587683511.png',
    './capture/1543587684011.png',
    './capture/1543587684511.png',
    './capture/1543587685011.png',
    './capture/1543587685511.png',
    './capture/1543587686012.png',
    './capture/1543587686511.png'

  ],
  index: 0
}

window.playbacktimer = window.setInterval(() => {
  if (window.currentPlaybackData.images.length > 0) {
    window.currentPlaybackData.index += 1
    if (window.currentPlaybackData.index >= window.currentPlaybackData.images.length) {
      window.currentPlaybackData.index = 0
    }
  }
}, 200)

export default {
  data () {
    return {playbackData: window.currentPlaybackData}
  },

  computed: {
    current_img () {
      if (this.playbackData.images.length > 0) {
        return this.playbackData.images[this.playbackData.index]
      } else {
        return ''
      }
    }
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
  stroke-dasharray: 320;
  stroke-dashoffset: 0;
  animation: pathplayback 3s linear infinite;
}
@keyframes pathplayback {
  0% {
    stroke-dashoffset: 320;
  }

  100% {
    stroke-dashoffset: 0;
  }
}
</style>

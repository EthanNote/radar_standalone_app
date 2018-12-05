<template>
  <div>
    <el-row :gutter="5">
       <el-col :xs="24" :sm="18" :md="12" :lg="12" :xl="12">
        <div class="grid-content bg-purple">
          <radar-plot></radar-plot>
        </div>
      </el-col>
       <el-col :xs="24" :sm="18" :md="12" :lg="12" :xl="12">
        <div class="grid-content bg-purple">
          <radar-video></radar-video>
        </div>
      </el-col>
    </el-row>
    <el-row :gutter="5">
      <el-col :span="24">
        <div class="grid-content bg-purple">
          <radar-frame-data></radar-frame-data>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import RadarPlot from './RadarMonitor/RadarPlot'
import RadarFrameData from './RadarMonitor/RadarFrameData'
import RadarVideo from './RadarMonitor/RadarVideo'

export default {
  name: 'radar-monitor',
  components: { RadarPlot, RadarFrameData, RadarVideo }
  //   methods: {
  //     open (link) {
  //       this.$electron.shell.openExternal(link);
  //     }
  //   }
}
</script>

<style>
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
  background: #99a9bf;
}
.bg-purple {
  background: #d3dce6;
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  padding: 5px;
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>

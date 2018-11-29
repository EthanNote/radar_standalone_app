<template>
  <el-row class="tac">
    <el-col :span="6">
      <div style="background-color:gray;padding:1em;color:white;margin-right:1em;font-weight:bold;font-size:20px">
    毫米波雷达安防系统
    </div>
    <el-menu
      default-active="2"
      class="el-menu-vertical-demo"
      @open="handleOpen"
      @close="handleClose">
      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>定位</span>
        </template>      
        <el-submenu index="1-1">
          <template slot="title">地图</template>
        </el-submenu>
        <el-submenu index="1-2">
          <template slot="title">轨迹</template>
        </el-submenu>
      </el-submenu>
      <el-submenu index="2">
        <template slot="title">
          <i class="el-icon-setting"></i>
          <span>设置</span>
        </template>      
        <el-submenu index="2-1">
          <template slot="title">设备</template>
        </el-submenu>
        <el-submenu index="2-2">
          <template slot="title">服务器</template>
        </el-submenu>
        <el-submenu index="2-3">
          <template slot="title">报警规则</template>
        </el-submenu>
      </el-submenu>
      <el-submenu index="3">
        <template slot="title">
          <i class="el-icon-document"></i>
          <span>指南</span>
        </template>      
        <el-submenu index="1-4">
          <template slot="title">设备调试</template>
        </el-submenu>
        <el-submenu index="1-4">
          <template slot="title">网络连接</template>
        </el-submenu>
        <el-submenu index="1-4">
          <template slot="title">参数设置</template>
        </el-submenu>
      </el-submenu>
      <el-submenu index="4">
        <template slot="title">
          <i class="el-icon-menu"></i>
          <span>应用</span>
        </template>      
        <el-submenu index="4-1">
          <template slot="title">安防警报</template>
        </el-submenu>
        <el-submenu index="4-2">
          <template slot="title">门禁统计</template>
        </el-submenu>
        <el-submenu index="4-3">
          <template slot="title">家庭看护</template>
        </el-submenu>
      </el-submenu>
     
    </el-menu>
  </el-col>
  <el-col :span="18">
  <el-tabs v-model="activeName" @tab-click="handleClick">
    <el-tab-pane label="设备监控" name="monitor">
        <radar-monitor></radar-monitor>
    </el-tab-pane>
    <el-tab-pane label="用户管理" name="first"><user-list></user-list></el-tab-pane>
    <el-tab-pane label="配置管理" name="second">配置管理</el-tab-pane>
    <el-tab-pane label="角色管理" name="third">角色管理</el-tab-pane>
    <el-tab-pane label="任务管理" name="fourth">任务管理</el-tab-pane>
  </el-tabs>
 </el-col>
  </el-row>
</template>
<script>
import SideMenu from './SideMenu'
import RadarMonitor from './RadarMonitor'
import UserList from './UserList'

export default {
  name: 'radar-home',
  components: {
    SideMenu,
    RadarMonitor,
    UserList
  },
  data () {
    return {
      activeName: 'second'
    }
  },
  methods: {
    handleClick (tab, event) {
    //   console.log(tab, event)
    }
  }
}
</script>
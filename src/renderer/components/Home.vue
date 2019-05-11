<template>
  <el-row class="tac">
    <div style="background-color:gray;padding:1em 0 1em 1em;color:white;font-weight:bold;font-size:20px;width: 100%"> 
      <span>毫米波雷达安防系统</span>
      <div style="float: right;padding-right: 1em;">{{this.states}}</div>
    </div>
    <el-col :span="3"
            background-color="#707070">
      <el-radio-group v-model="isCollapse" style="margin-bottom: 5px;margin-top: 5px">
        <div class="button">
          <el-radio-button type="text" :label="false"><span class="iconfont">&#xe68a;</span></el-radio-button>
          <el-radio-button type="text" :label="true"><span class="iconfont">&#xe6bf;</span></el-radio-button>
        </div>
      </el-radio-group>
      <el-menu default-active="1-1" 
         class="el-menu-vertical-demo" 
         @open="handleOpen" 
         @close="handleClose" 
         :collapse="isCollapse"
         :collapse-transition ="false"
         >
        <el-submenu index="1">
          <template slot="title">
            <i class="el-icon-location"></i>
            <span slot="title">定位</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="1-1">
              <span class="iconfont">&#xe620;</span>
              <template slot="title">地图</template>
            </el-menu-item>
            <el-menu-item index="1-2">
              <span class="iconfont">&#xe61c;</span>
              <template slot="title">轨迹</template>
            </el-menu-item>
          </el-menu-item-group>
        </el-submenu>
        <el-submenu index="2">
          <template slot="title">
            <i class="el-icon-setting"></i>
            <span slot="title">设置</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="2-1">
              <span class="iconfont">&#xe65e;</span>
              <template slot="title">设备</template>
            </el-menu-item>
            <el-menu-item index="2-2">
              <span class="iconfont">&#xe60a;</span>
              <template slot="title">服务器</template>
            </el-menu-item>
            <el-menu-item index="2-3">
              <span class="iconfont">&#xe62b;</span>
              <template slot="title">报警规则</template>
            </el-menu-item>
          </el-menu-item-group>
        </el-submenu>
        <el-submenu index="3">
          <template slot="title">
            <i class="el-icon-document"></i>
            <span slot="title">指南</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="3-1">
              <span class="iconfont">&#xe60b;</span>
              <template slot="title">设备调试</template>
            </el-menu-item>
            <el-menu-item index="3-2">
              <span class="iconfont">&#xe659;</span>
              <template slot="title">网络连接</template>
            </el-menu-item>
            <el-menu-item index="3-3">
              <span class="iconfont">&#xe608;</span>
              <template slot="title">参数设置</template>
            </el-menu-item>
          </el-menu-item-group>
        </el-submenu>
        <el-submenu index="4">
          <template slot="title">
            <i class="el-icon-menu"></i>
            <span slot="title">应用</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="4-1">
              <span class="iconfont">&#xe65b;</span>
              <template slot="title">安防警报</template>
            </el-menu-item>
            <el-menu-item index="4-2">
              <span class="iconfont">&#xe63e;</span>
              <template slot="title">门禁统计</template>
            </el-menu-item>
            <el-menu-item index="4-3">
              <span class="iconfont">&#xe697;</span>
              <template slot="title">家庭看护</template>
            </el-menu-item>
          </el-menu-item-group>
        </el-submenu>
      </el-menu>
    </el-col>
    <el-col  style="padding-left: 20px;width: 85%">
      <el-tabs v-model="activeName" @tab-click="handleClick" >
        <el-tab-pane label="设备监控" name="first">
          <div style="display: flex;">
            <div style="width: 80%">
              <radar-monitor></radar-monitor>
            </div>
            <div style="width: 20%">
              <connection></connection>
            </div>
          </div>
        </el-tab-pane>
        <el-tab-pane label="用户管理" name="second">
          <user-list></user-list>
        </el-tab-pane>
        <el-tab-pane label="记录回放" name="third">
          <play-back></play-back>
        </el-tab-pane>
      <!--  <el-tab-pane label="连接管理" name="fourth">
          <connection></connection>
        </el-tab-pane> -->
        <el-tab-pane label="警报邮件" name="fourth">
          <warn-notify></warn-notify>
        </el-tab-pane>
        <el-tab-pane label="进程管理" name="fifth">
          <workers></workers>
        </el-tab-pane>
        <el-tab-pane label="隧道测距" name="sixth">
          <tunnel></tunnel>
        </el-tab-pane>
        <el-tab-pane label="帧统计" name="sevenh">
          <frame-statics></frame-statics>
        </el-tab-pane>
        <el-tab-pane label="区外离线检测" name="eighth">
          <transection-monitor></transection-monitor>
        </el-tab-pane>
        <el-tab-pane label="警报管理" name="ninth">
          <warn-management></warn-management>
        </el-tab-pane>
        <el-tab-pane label="警报消息记录" name="tenth">
          <warn-message></warn-message>
        </el-tab-pane>
      </el-tabs>
    </el-col>
  </el-row>
</template>
<script>
import SideMenu from './SideMenu'
import RadarMonitor from './RadarMonitor'
import UserList from './UserList'
import PlayBack from './PlayBack'
import WarnNotify from './WarnNotify'
import Connection from './Connection'
import Workers from './Workers'
import Tunnel from './Tunnel'
import FrameStatics from './FrameStatics'
import TransectionMonitor from './TransectionMonitor'
import WarnManagement from './WarnManagement'
import WarnMessage from './WarnMessage/WarnMessage'
export default {
  name: 'radar-home',
  components: {
    SideMenu,
    RadarMonitor,
    UserList,
    PlayBack,
    WarnNotify,
    Connection,
    Workers,
    Tunnel,
    FrameStatics,
    TransectionMonitor,
    WarnManagement,
    WarnMessage
  },
  data () {
    return {
      activeName: 'first',
      isCollapse: false,
      states: '未连接'
    }
  },
  methods: {
    handleClick (tab, event) {
      //   console.log(tab, event)
    },
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    }
  },
  mounted () {
    window.eventBus.$on('link', (status) => {
      this.states = status
      console.log(status)
    })
  }
}
</script>

<style>
  .pane-first.el-tab-pane {
    display: flex !important;
  }
</style>

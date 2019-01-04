<template>
  <div>
    <h3>进程管理</h3>
   
    <el-row>
      <el-table :data="processList" height="250" border style="width: 100%">
        <el-table-column prop="name" label="名称" width="180"></el-table-column>
        <el-table-column prop="state" label="状态" width="180"></el-table-column>
        <el-table-column prop="command" label="命令" ></el-table-column>
        <el-table-column fixed="right" label="操作" width="100">
          <template slot-scope="scope">
            <el-button @click="commandStart(processList[scope.$index].name)" type="text" size="small">启动</el-button>
            <el-button @click="commandStop(processList[scope.$index].name)" type="text" size="small">停止</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-row>
  </div>
</template>
<script>
var dgram = require('dgram')
var udpClient = dgram.createSocket('udp4')

export default {
  data () {
    return {
      processList: [{ name: '', state: 0 }]
    }
  },
  created () {
    var self = this
    udpClient.on('message', function (msg, rinfo) {
      try {
        var data = JSON.parse(msg)

        if (data) {
          self.processList = data
        }
      } catch (e) {}
      console.log(
        `receive message from ${rinfo.address}:${rinfo.port}：${msg}`
      )
    })

    window.setInterval(self.fetchState, 1000)
  },
  methods: {
    fetchState () {
      var SendBuff = '{"client":true}'
      var SendLen = SendBuff.length
      udpClient.send(SendBuff, 0, SendLen, 7788, '127.0.0.1')
    },
    commandStart (name) {
      var SendBuff = `{"action":"run", "name":"${name}"}`
      var SendLen = SendBuff.length
      udpClient.send(SendBuff, 0, SendLen, 7788, '127.0.0.1')
      console.log(SendBuff)
      this.fetchState()
    },
    commandStop (name) {
      var SendBuff = `{"action":"kill", "name":"${name}"}`
      var SendLen = SendBuff.length
      udpClient.send(SendBuff, 0, SendLen, 7788, '127.0.0.1')
      console.log(SendBuff)
      this.fetchState()
    }
  }
}
</script>

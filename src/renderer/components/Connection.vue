<template>
  <div>
    <h1>连接</h1>
    <div>{{ status }}</div>
    <div v-for="r in history">
      <h3>{{ r.time }}</h3>
      <el-input type="textarea" :autosize="{ minRows: 4, maxRows: 15}" :value="r.content.toString()"></el-input>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      history: [],
      status: '未连接'
    }
  },

  methods: {
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
    }

  },

  created () {
    var self = this
    /* 创建简单的UDP服务器 */
    var dgrm = require('dgram')
    var server = dgrm.createSocket('udp4') // udp4为指定UDP通信的协议类型
    server.on('message', function (msg, rinfo) {
      self.status = ('收到消息，长度 = ' + msg.length).toString()
      var date = new Date()
      date.setDate(date.getDate() + 1)
      self.history = [{time: self.formatDate(date), content: msg}].concat(self.history)
    })
    // 当socket对象开始监听指定的端口和地址时，触发socket端口的listening事件
    /* server.on('listening',function () {
    var address = server.address();
    console.log('服务器开始监听。地址信息为&j',address);
    }); */
    server.bind(3000, 'localhost', function () {
      // bind方法中也可以不写回调函数，单独监听listening事件
      var address = server.address()
      self.status = ('已启动，地址：' + address.address + ':' + address.port).toString()
    })
  }
}
</script>




<style>
.message {
  width: 100%;
  border: 1px solid gray;
}
</style>

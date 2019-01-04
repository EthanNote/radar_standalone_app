<template>
  <div>
    <h1>连接</h1>
    <el-button @click="connect" type="text" size="small">连接</el-button>
    <div>{{ status }}</div>
    <div v-for="r in history">
      <h3>{{ r.time }}</h3>
      <div>format = {{ r.format }}</div>
      <el-input
        type="textarea"
        :autosize="{ minRows: 4, maxRows: 15}"
        :value="r.content.toString()"
      ></el-input>
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
    },

    connect () {
      var self = this
      this.client.connect(
        6666,
        'localhost',
        function () {
          console.log('Connected to server')
          self.status = '已连接'
          var command = '{"rename":"ELECTRON_CLIENT"}'
          self.client.write('' + command.length + ':' + command + ',')
        }
      )

      this.client.on('data', function (data) {
        console.log('>' + data)
        var msg = data.replace(/[0-9][0-9]*:/, '').replace(/,$/, '')
        self.status = ('收到消息，长度 = ' + msg.length).toString()
        var date = new Date()
        // date.setDate(date.getDate() + 1)

        var parsed = JSON.parse(msg)
        var format = 'string'
        if (parsed) {
          format = 'JSON'
          if (parsed.emit) {
            window.eventBus.$emit(parsed.emit.event, parsed.emit.args)
          }
        }
        self.history = [
          { time: self.formatDate(date), format: format, content: msg }
        ].concat(self.history)
      })
    }
  },

  created () {
    var self = this
    /* 创建简单的UDP服务器 */
    // var dgrm = require('dgram')
    var net = require('net')
    var client = new net.Socket()
    self.client = client
    client.setEncoding('ascii')

    window.eventBus.$on('console.log', arg => {
      console.log(arg)
    })

    // var server = dgrm.createSocket('udp4') // udp4为指定UDP通信的协议类型
    // server.on('message', function (msg, rinfo) {
    //   self.status = ('收到消息，长度 = ' + msg.length).toString()
    //   var date = new Date()
    //   date.setDate(date.getDate() + 1)
    //   self.history = [{time: self.formatDate(date), content: msg}].concat(self.history)
    // })
    // // 当socket对象开始监听指定的端口和地址时，触发socket端口的listening事件
    // /* server.on('listening',function () {
    // var address = server.address();
    // console.log('服务器开始监听。地址信息为&j',address);
    // }); */
    // server.bind(3000, 'localhost', function () {
    //   // bind方法中也可以不写回调函数，单独监听listening事件
    //   var address = server.address()
    //   self.status = ('已启动，地址：' + address.address + ':' + address.port).toString()
    // })
  }
}
</script>




<style>
.message {
  width: 100%;
  border: 1px solid gray;
}
</style>

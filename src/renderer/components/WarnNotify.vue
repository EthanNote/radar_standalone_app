<template>
  <div>
    <!-- <input
      type="text"
      v-model="event_type"
    >

    <input
      type="text"
      v-model="details"
      @keyup.enter="sendEmail"
    > -->
    <!-- <el-input
      type="textarea"
      autosize
      placeholder="请输入警报类型"
      v-model="event_type"
    >
    </el-input> -->
    <el-select
      v-model="value"
      placeholder="请选择警报类型"
    >
      <el-option
        v-for="item in options"
        :key="item.value"
        :label="item.label"
        :value="item.value"
      >
      </el-option>
    </el-select>
    <div style="margin: 20px 0;"></div>
    <el-input
      type="textarea"
      :autosize="{ minRows: 7, maxRows: 300}"
      placeholder="请输入警报内容"
      v-model="details"
      @keyup.enter="sendEmail"
    >
    </el-input>
    <div class="button-row">
      <el-button
        class="send-button"
        type="primary"
        @click="sendEmail"
      >发送邮件</el-button>
    </div>
  </div>
</template>

<script>
export default {
  //   name: 'user-list',
  data () {
    return {
      details: '',
      options: [{
        value: '黑客入侵',
        label: '黑客入侵'
      }, {
        value: '人员伤亡',
        label: '人员伤亡'
      }, {
        value: '员工早退',
        label: '员工早退'
      }, {
        value: '地球末日',
        label: '地球末日'
      }, {
        value: '该吃饭了',
        label: '该吃饭了'
      }],
      value: ''
    }
  },
  methods: {
    sendEmail () {
      var self = this
      self.emailjs.init('user_r9Jpncka45g6pvtbz76yg')
      if (self.value !== '' && self.details !== '') {
        self.emailjs.send('smtp_server', 'radar_system_notification', { 'event_type': this.value, 'details': this.details, 'ejs_dashboard__test_template': true }).then(
          function (response) {
            self.$message({
              message: '邮件发送成功！',
              type: 'success'
            })
          }
          , function (error) {
            self.$message.error('发送失败！' + error)
          }
        )
        self.$message({
          message: '邮件正在发送...'
        })
      } else {
        alert('请输入内容！！')
      }
    }
  },
  created () {
    this.emailjs = require('emailjs-com')
  }
}
</script>


<style>
.button-row {
  padding-top: 1em;
}

.send-button {
  float: right;
}
</style>

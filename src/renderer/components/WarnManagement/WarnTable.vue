<template>
  <table class="table">
    <tr class="text">
      <td class="tab">位置</td>
      <td class="tab">横坐标X</td>
      <td class="tab">纵坐标Y</td>
    </tr>
    <tr class="text">
      <td class="tab">当前位置</td>
      <td class="tab">{{this.x1}}</td>
      <td class="tab">{{this.y1}}</td>
    </tr>
  </table>
</template>

<script>
export default {
  name: 'warn-table',
  data () {
    return {
      x1: 0,
      y1: 0
    }
  },
  mounted () {
    window.eventBus.$on('dot', (arg) => {
      this.x1 = arg.x
      this.y1 = arg.y
    })
  }
}
</script>

<style>
.tab {
  width: 200px;
}
.text {
  margin-top: 10px;
}
.table {
  margin-top: 100px;
  border: 2px solid #f1f1f1;
  text-align: center;
  display: block;
}
</style>

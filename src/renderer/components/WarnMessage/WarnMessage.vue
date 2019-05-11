<template>
  <el-table :data="contents" stripe class="animated bounceInUp">
    <el-table-column v-for="(item, index) in contentsTitle" :key="index" :label="item">
      <template scope="scope">
        <span>{{scope.row[index]}}</span>
      </template>
    </el-table-column>
  </el-table>
</template>
<script>
export default {
  name: 'warn-message',
  data () {
    return {
      contentsTitle: ['时间', '位置', '事件'],
      contents: []
    }
  },
  methods: {
  },
  mounted () {
    window.eventBus.$on('warnning', (message) => {
      console.log(message)
      this.contents.push(message)
    })
  }
}
</script>

<style>

</style>
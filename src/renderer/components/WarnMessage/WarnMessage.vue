<template>
  <el-table :data="contents" 
            stripe>
    <el-table-column v-for="(item, index) in contentsTitle" :key="index" :label="item">
      <template scope="scope">
        <span style="margin-left: 10px">{{scope.row[index]}}</span>
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
    window.eventBus.$on('warnning', (event) => {
      console.log(event)
      this.contents.push(event)
    })
  }
}
</script>

<style>

</style>
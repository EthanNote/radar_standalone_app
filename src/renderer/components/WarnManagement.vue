<template>
  <div >
    <warn-header></warn-header>
    <warn-management1></warn-management1>
    <warn-table></warn-table>
  </div>
</template>

<script>
import WarnHeader from './WarnManagement/WarnHeader'
import WarnManagement1 from './WarnManagement/WarnManagement1'
import WarnTable from './WarnManagement/WarnTable'
export default {
  name: 'warn-management',
  components: {
    WarnManagement1,
    WarnHeader,
    WarnTable
  },
  data () {
    return {
    }
  }
}
</script>

<style>
</style>

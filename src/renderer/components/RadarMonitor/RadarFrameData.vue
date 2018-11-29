<template>
  <div>
    <h3>数据记录</h3>
    <el-table
      :data="tableData"
      style="width: 100%">
      <el-table-column
        prop="index"
        label="Index"
        width="180">
      </el-table-column>
      <el-table-column
        prop="id"
        label="ID"
        width="180">
      </el-table-column>
      <el-table-column
        prop="location"
        label="Location">
      </el-table-column>
    </el-table>
  </div>
  </template>

  <script>
    export default {
      data () {
        return {
          tableData: [{
            index: '0',
            id: '1',
            location: '0,0'
          }, {
            index: '1',
            id: '1',
            location: '0,0'
          }, {
            index: '2',
            id: '2',
            location: '0,0'
          }, {
            index: '3',
            id: '2',
            location: '0,0'
          }]
        }
      }
    }
  </script>
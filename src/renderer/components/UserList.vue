<template>
    <el-table
      :data="tableData"
      style="width: 100%">      
      <el-table-column
        prop="name"
        label="姓名"
        width="180">
      </el-table-column>
      <el-table-column
        prop="address"
        label="单位">
      </el-table-column>
      <el-table-column
        prop="date"
        label="注册时间"
        width="180">
      </el-table-column>
    </el-table>
  </template>

  <script>
    export default {
      name: 'user-list',
      data () {
        return {
          tableData: [{
            date: '2016-05-02',
            name: '管理员1',
            address: '西安市众创示范街区 A111'
          }, {
            date: '2016-05-02',
            name: '管理员2',
            address: '西安市众创示范街区 A111'
          }, {
            date: '2016-05-02',
            name: '管理员3',
            address: '西安市众创示范街区 A111'
          }, {
            date: '2016-05-02',
            name: '管理员4',
            address: '西安市众创示范街区 A111'
          }]
        }
      }
    }
  </script>
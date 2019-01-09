<template>
    <div>
        <el-table
            :data="this.user.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
            style="width: 100%"
            :default-sort="{prop: 'createdDate', order: 'descending'}"
        >
            <el-table-column
                label="姓名"
                width="180"
            >
                <template slot-scope="scope">
                    <span style="margin-left: 10px">{{ scope.row.name }}</span>
                </template>
            </el-table-column>
            <el-table-column
                prop="email"
                label="电子邮件"
                width="180"
            >
            </el-table-column>
            <el-table-column
                prop="createdDate"
                sortable
                label="注册时间"
            >
            </el-table-column>
            <el-table-column
                prop="level"
                label="权限级别"
                sortable
            >
                <template slot-scope="scope">
                    <el-button
                        type="success"
                        round
                        size="medium"
                        v-show="scope.row.level === 'admin'"
                    >Admin</el-button>
                    <el-button
                        type="default"
                        round
                        size="medium"
                        v-show="scope.row.level === 'user'"
                    >User</el-button>

                </template>
            </el-table-column>
            <el-table-column align="right">
                <template
                    slot="header"
                    slot-scope="scope"
                >
                    <el-input
                        v-model="search"
                        size="mini"
                        placeholder="输入姓名关键字搜索"
                    />
                </template>
                <template slot-scope="scope">
                    <!-- <el-button
                        size="mini"
                        @click="handleEdit(scope.$index, scope.row)"
                    >Edit</el-button> -->
                    <el-button
                        size="mini"
                        type="danger"
                        @click="handleDelete(scope.$index, scope.row)"
                    >Delete</el-button>
                </template>
            </el-table-column>
        </el-table>
    </div>
</template>
<script>
import axios from 'axios'
export default {
  data () {
    return {
      search: ''
    }
  },
  created () {
    // axios.get('https://easy-mock.com/mock/5c3585321776390cf4a22824/user/').then(response => {
    //   console.log(response)
    //   this.users = response.data
    // })
    // console.log(this.user)
  },
  methods: {
    handleEdit (index, row) {
      console.log(index, row)
    },
    handleDelete (index, row) {
      console.log(index, row)
      if (row.level === 'admin') {
        alert('不能删除管理员!')
      } else {
        this.users.splice(index, 1)
        axios.post('https://easy-mock.com/mock/5c3585321776390cf4a22824/user/', this.users).then(response => {
          console.log(response)
        })
      }
    }
  }
}
</script>
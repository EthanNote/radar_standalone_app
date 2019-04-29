<template>
  <div>
    <h2>警报区域设置</h2>
    <div class="pic">
      <div><img  src="./img/2.png">     监控区域</div>
      <div class="img"><img  src="./img/1.png">     禁止区域</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'warn-header'
}
</script>

<style>
.pic {
  display: flex;
  font-size: 12px;
}
.img {
  margin-left: 60px;
}
</style>

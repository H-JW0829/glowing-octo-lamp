<template>
  <div id="app">
    <div id="nav">
        <div id='left'>
          <blogHeader></blogHeader>
        </div>
        <div id='right'>
          <clock></clock>
        </div>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
// @ is an alias to /src
import addBlog from '@/components/AddBlog.vue'
import showBlogs from '@/components/ShowBlogs.vue'
import blogHeader from '@/components/BlogHeader.vue'
import login from '@/components/Login.vue'
import clock from  '@/components/clock.vue'
export default {
  name: 'App',
  components: {
    addBlog,
    showBlogs,
    blogHeader,
    login,
    clock
  },
  data(){
  }
}
</script>



<style scoped type="text/css">
  #app{
    font-family:Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing:antialiased;
    -moz-osx-font-smoothing:grayscale;
    text-align:center;
    color:#2c3e50;
    /*margin-top:60px;*/
    overflow:hidden;
    }

  #left,#right{
    display: inline-block;
  }

  #right{
    float: right;
    position: absolute;
    right: 100px;
    top:20px;
  }
</style>

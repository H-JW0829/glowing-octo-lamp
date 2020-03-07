<template>
  <div id="app">
    <div id="nav">
        <blogHeader></blogHeader>
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
export default {
  name: 'App',
  components: {
    addBlog,
    showBlogs,
    blogHeader,
    login
  }
}
</script>


<style lang="stylus">
#app
  font-family Avenir, Helvetica, Arial, sans-serif
  -webkit-font-smoothing antialiased
  -moz-osx-font-smoothing grayscale
  text-align center
  color #2c3e50
  margin-top 60px
  overflow hidden

</style>

<template>
  <div class="addBlog">
    <h2>添加博客</h2>
    <form v-if="!isSubmit">
      <label>博客标题</label>
      <input type="text" v-model="blog.title" required>

      <label>博客内容</label>
      <textarea v-model="blog.content" required></textarea>

      <div id="checkboxes">
        <label>Html</label>
        <input type="checkbox" value="Html" v-model="blog.categories">
        <label>JavaScript</label>
        <input type="checkbox" value="JavaScript" v-model="blog.categories">
        <label>CSS</label>
        <input type="checkbox" value="CSS" v-model="blog.categories">
        <label>Vue</label>
        <input type="checkbox" value="Vue" v-model="blog.categories">
      </div>
      
      <label style="padding-top: 10px">作者</label>
      <select v-model="blog.author" required>
        <option v-for="(author,index) in authors" :key="index">{{author}}</option>
      </select>
      <button @click="submit($event)">添加博客</button>
    </form>

  </div>
</template>

<script>
import Vue from '../main.js'
import axios from 'axios'  
export default {
  name: 'addBlog',
  data(){
    return{
      isSubmit:false, //是否提交博客
      blog:{         //博客内容
        title:"",
        content:"",
        categories:[],
        author:""
      }
    }
  },
  methods:{
    submit($event){
        if(this.blog.title != "" && this.blog.content != ""){ //当博客的标题和内容都不为空时才能提交
        $event.preventDefault(); 
        var that = this;      //发送axios请求到后端，提交数据
        axios({
              method: 'post',
              url: '/api/add_blog',
              data: that.blog,
            })
            .then((response) => {
                  Vue.prototype.$message.success("添加博客成功~");
                  this.$router.replace({path:'/'});    //提交完成后回到博客首页
            })
            .catch((error) => {
                  Vue.prototype.$message.warning("对不起，发生异常，请稍后再试或联系管理员~");
            })

      }
    }
  },
  computed:{
    authors(){
      return this.$store.state.authors;   //拿到存储在vuex中的user名称，作为博客的author
    }
  },
  created(){
    this.$store.dispatch('getAuthors');   //调用vuex getAuthors方法，得到数据库中的所有作者列表
  },
  props: {
    
  }
}
</script>
<style scoped type="text/css">
.addBlog *{
  box-sizing: border-box;
}

.addBlog{
  margin:20px auto;
  width: 800px;
  padding: 20px;
  background:#428bca;
  height: 580px;
}

form>label{
  display: block;
  margin:20px 0 10px;
  font-weight: 900;
}

input[type="text"],textarea,select{
  display: block;
  width:100%;
  padding: 6px;
  border-radius: 5px;
  border:1px solid black ;
}

input[type="text"],textarea{
    font-size:18px;
}

textarea{
  height: 300px;
}

#checkboxes label{
  display: inline-block;
  margin-top: 0px;
}

#checkboxes input{
  display: inline-block;
  margin-right: 10px;
}

#checkboxes *{
  float: left;
}

button{
  display: block;
  margin:40px 0;
  color:#fff;
  font-size: 15px;
  cursor: pointer;
  float: right;
  background: #428bca;
  border-radius: 5px;
  padding: 8px;
  border: 1px solid transparent;  
}

</style>

<template>
  <div class="addBlog">
    <h2>编辑博客</h2>
    <form v-if="!isSubmit">
      <label>博客标题</label>
      <input type="text" v-model="blog.title" required>

      <label>博客内容</label>
      <textarea v-model="blog.content" required></textarea>

      <div id="checkboxes">
        <label>Html</label>
        <input type="checkbox" value="Html" v-model="blog.category">
        <label>JavaScript</label>
        <input type="checkbox" value="JavaScript" v-model="blog.category">
        <label>CSS</label>
        <input type="checkbox" value="CSS" v-model="blog.category">
        <label>Vue</label>
        <input type="checkbox" value="Vue" v-model="blog.category">
      </div>

      <label style="padding-top: 10px">作者</label>
      <select v-model="blog.author">
        <option v-for="(author,index) in authors" :key="index">{{author}}</option>
      </select>
      <button @click="submit($event)">确定</button>
    </form>

    <div v-if="isSubmit">
      <p>{{msg}}</p>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import Vue from '../main.js'
export default {
  name: 'addBlog',
  data(){
    return{
      isSubmit:false,
      id:this.$route.params.id,
      blog:{},
      authors:["小黄","小钟"],
      msg:""
    }
  },
  methods:{
    submit($event){ //提交编辑好的博客到后端
      $event.preventDefault();
      var that = this;
      axios({
            method: 'post',
            url: '/api/edit_blog',
            data: that.blog,
          })
          .then((response) => {
                that.isSubmit = true;
                that.msg = response['data']['msg'];
          })
          .catch((error) => {
                Vue.prototype.$message.warning("对不起，发生异常，请稍后再试或联系管理员~");
          })
    }
  },
  props: {
    
  },
  created(){
      //获取这条博客的数据
      var that = this;
      axios.get('/api/get_single_blog',{params:{"id":that.id}})
      .then((response)=>{
              if(response['data'][0]['status'] === "200"){
                that.blog = response['data'][1];
                that.blog.category = that.blog.category.split('-');
              }else{
                Vue.prototype.$message.warning("获取数据出错了~~~")
              }
        })
        .catch((response)=>{
            Vue.prototype.$message.warning("系统发生了异常，请稍后重试~")
        })
  }
}
</script>
<style scoped type="text/css">
<style scoped type="text/css">
.addBlog *{
  box-sizing: border-box;
}

.addBlog{
  margin:20px auto;
  width: 800px;
  padding: 20px;
  background:#428bca;
  height: 600px;
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

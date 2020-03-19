<template>
  <div id="showBlogs">
    <div id="mynav">
        <a href="javascript:void(0)" @click="showMyBlogs()">我的博客</a> | 
        <a href="javascript:void(0)" @click="showMyFavorite()">我的收藏</a>
    </div>
    <div v-for="(blog,index) in pageBlogs" :key="index" id="single-blog">
      <div id="blog_div">
        <router-link :to="'/blog/' + blog.id + '/' + canDelete">
          <h2 v-rainbow>{{blog.title | toUpper}}</h2>
        </router-link>
        <article>
          {{blog.content | lessSentences}}
        </article>
    </div>
    </div>
    <div id="pagination">
        <p><a href="javascript:void(0);" style="text-decoration: none" @click="ChangePage(0)">上一页</a>  |
            <a href="javascript:void(0);" style="text-decoration: none" @click="ChangePage(1)">下一页</a></p>
    </div>
  </div>
</template>

<script>
import axios from 'axios' 
import Vue from '../main.js' 
import {changeData} from '../assets/JS/myUtils'
export default {
  name: 'showBlogs',
  data(){
    return{
      blogs:[],
      search:"",
      maxPageSize:7,
      page:1,
      PageBlogs:this.pageBlogs,
      canDelete:1,
      favoriteBlogs:[], //我收藏的博客    
      myBlogs:[]    //我的博客
    }
  },
  methods:{
      initPageBlogs(){
        let pageBlogs = [];
        if(this.blogsSize > this.maxPageSize){
            let start = (this.page - 1) * this.maxPageSize;
            let end = start + this.maxPageSize;
            pageBlogs = this.blogs.slice(start, end); 
        }else{
          pageBlogs = this.blogs;
        }
        return pageBlogs;
      },
      ChangePage(flag){
        let arr = changeData(flag,this.blogs,this.PageBlogs,this.page,this.maxPageSize,this.blogsSize);
        this.page = arr[0];
        this.PageBlogs = arr[1];
      },
      showMyBlogs(){
          this.blogs = this.myBlogs;
          this.canDelete = 1;
      },
      showMyFavorite(){
          this.blogs = this.favoriteBlogs;
          this.canDelete = 0;
      }
  },
  created(){
    //获取我的博客
    axios({
            method: 'post',
            url: '/api/get_personal_blogs',
            data:{
              'user':window.sessionStorage.user
            }
        })
      .then((response) => {
          if(response['data'][0]['status'] === '200'){
              let datas = response['data'].slice(1);
              for(let data of datas){
                  this.myBlogs.push(data);
              }
              this.blogs = this.myBlogs;
          }else{
            Vue.prototype.$message.warning("加载数据出了点问题，请咨询管理员~")
          }
      })
      .catch((error) => {
          Vue.prototype.$message.warning("对不起，发生异常，请稍后再试或联系管理员~");
      }),

      //获取我收藏的博客
      axios({
            method: 'post',
            url: '/api/get_favorite_blogs',
            data:{
              'user':window.sessionStorage.user
            }
        })
      .then((response) => {
          if(response['data'][0]['status'] === '200'){
              let datas = response['data'].slice(1);
              for(let data of datas){
                  this.favoriteBlogs.push(data);
              }
          }else{
            Vue.prototype.$message.warning("加载数据出了点问题，请咨询管理员~")
          }
      })
      .catch((error) => {
          Vue.prototype.$message.warning("对不起，发生异常，请稍后再试或联系管理员~");
      })

      },
  computed:{
    pageBlogs:function(){
      return this.initPageBlogs();
    },
    blogsSize:function(){
      return this.blogs.length;
    }
  },
  props: {
    
  }
}
</script>
<style scoped type="text/css">
#showBlogs{
  max-width: 800px;
  margin:0 auto;
}

#blog_div{
  background-image: url("@/../../assets/bg.jpg");
  padding: 10px;
}

#single-blog{
  padding: 20px;
  margin:20px 0;
  box-sizing: border-box;
  background:  #428bca;
  border:1px dotted #aaa;
}

#showBlogs a{
  text-decoration: none;
  color:#444;
}

input[type="text"]{
  padding: 6px;
  width: 100%;
  box-sizing: border-box;
}

#searchBar{
  border-radius: 3px;
}
#pagination{
  float:right;
}
#pagination>p a:hover{
  color:blue;
}
#mynav{
  box-sizing: border-box;
  background:#428bca;
  height:38px;
  color:#fff;
  padding-top:10px; 
  margin:10px auto;
}
#mynav>a:hover{
  background:rgba(255,255,255,0.8);
  color:#444;
  padding: 5px 8px;
  border-radius: 5px;
}
</style>

<template>
  <div id="showBlogs">
    <h1>博客总览</h1>
    <input id="searchBar" type="text" v-model="search" placeholder="搜索...">
    <div v-for="(blog,index) in pageBlogs" :key="index" id="single-blog">
      <div class="single_blog" id="blog_div">
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
      canDelete:0,
      imgNum:0,
    }
  },
  methods:{
      initPageBlogs(){   //这个函数用于初始化第一页的数据
        let pageBlogs = [];
        if(this.blogsSize > this.maxPageSize){
            let start = (this.page - 1) * this.maxPageSize;
            let end = start + this.maxPageSize;
            pageBlogs = this.searchBlogs.slice(start, end); 
        }else{
          pageBlogs = this.searchBlogs;
        }
        return pageBlogs;
      },
      ChangePage(flag){ //当点击翻页时，这个函数更新PageBlogs中的数据，用于展示新的一页
        let arr = changeData(flag,this.blogs,this.PageBlogs,this.page,this.maxPageSize,this.blogsSize);
        this.page = arr[0];
        this.PageBlogs = arr[1];
      },
  },
  created(){ //从后端获取到所有的博客
     axios.get('/api/get_all_blogs').then((response)=>{
          if(response['data'][0]['status'] === '200'){
              let datas = response['data'].slice(1);
              for(let data of datas){
                  this.blogs.push(data);
              }
          }else{
            Vue.prototype.$message.warning("加载数据出了点问题，请咨询管理员~")
          }
        }).catch((response)=>{
          Vue.prototype.$message.warning("系统发生了异常，请您稍后再试~")
        })
  },
  mounted(){
  },
  computed:{
    searchBlogs:function(){  //过滤器，返回标题中有搜索词的博客
      return this.blogs.filter((blog) => {
        return blog.title.match(this.search);
      })
    },
    pageBlogs:function(){
      return this.initPageBlogs();
    },
    blogsSize:function(){
      return this.searchBlogs.length;
    },
    viewHeight:function(){
     return window.innerHeight || document.documentElement.clientHeight
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
</style>

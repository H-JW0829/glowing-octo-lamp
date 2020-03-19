<template>
	<div id="single-blog">
		<div id = "blog-detail">
			<div class="star" @click="changeState()" v-if="ison === 0"> 
				<i class="el-icon-star-off"></i>
			</div>
			<div class="star" v-if="ison === 1"> 
				<i class="el-icon-star-on"></i>
			</div>
			<h1>{{blog.title}}</h1>
			<p id="blog_content">{{blog.content}}</p>
			<hr>
			<p>
				<span id="category">分类：{{this.blog.categories_show}}</span>
				<span id="author">作者：{{blog.author}}</span>
			</p>
			<div id="myButton" v-if="canDelete == '1'">
				<button @click = "editBlog">编辑</button>
				<button @click = "deleteBlog">删除</button>
			</div>
		<div id = "blog-comments">
			<h3>评论（{{commentsLength}}）</h3>	
			<div id="comment-input">
                <el-input placeholder="请输入内容" v-model="comment"></el-input>
                <div style="text-align: right">
                	<button type="primary" plain size="medium" id="comment-button" @click="submitComment()">发布</button>
                </div>
            </div>
            <div id="comments-list" v-for="(comment,index) in pageComments" :key="index">
            	<div class='avater'> 
            		<img ref="avater" class="pic" alt="加载中">
            	</div>
            	<div class='info'>
	            	<div>
	            		<span style="margin-left:-84%;font-size:12px;color:#9b9b9b;">{{comment.authorName}} </span>
	            		<span style="float:right;font-size:12px;color:#9b9b9b;">{{comment.createTime}} </span>
	            	</div>
	            	<p style="text-align:left;margin:5px 0 10px">{{comment.content}}</p>
            	</div>
            </div>	
            <div id="pagination">
		        <p><a href="javascript:void(0);" style="text-decoration: none" @click="ChangePage(0)">上一页</a>  |
		            <a href="javascript:void(0);" style="text-decoration: none" @click="ChangePage(1)">下一页</a></p>
    		</div>
		</div>
		</div>
	</div>
</template>

<script type="text/javascript">
	import Vue from '../main.js'
	import axios from 'axios' 
	import {changeData} from '../assets/JS/myUtils'
	import logo from '../assets/avarter.png'
	export default{
		name:"single-blog",
		data(){
			return{
				id:this.$route.params.id, //获取到博客的id
				blog:{},
				comment:"",
				blogComments:[],
				maxPageSize:10,
     			page:1,
      			pageComments:[],
      			canDelete:this.$route.params.canDelete,
      			ison:0,
      			logo:logo,
      			num:0
			}
		},
		methods:{
			deleteBlog(){
				this.$confirm('您确定要删除吗？', '提示', {  //删除博客，把博客id传到后端，后端进行删除操作
	      				confirmButtonText: '确定',
	      				cancelButtonText: '取消',
	      				type: 'warning'
	     			}).then(() => {
						axios.get('/api/delete_blog',{params:{"id":this.id}})
						.then((response)=>{
					  			Vue.prototype.$message.warning(response['data']['msg']);
					  			this.$router.push({path:'/'});
			    			})
			    			.catch((response)=>{
			        			Vue.prototype.$message.warning("系统发生了异常，请稍后重试~")
			   				})
	     			}).catch(() => {
	    		});     
			},
			editBlog(){
				this.$router.push({path:'/edit-blog/' + this.id}); //编辑博客路由跳转到编辑界面
			},
			ChangePage(flag){
				//翻页，flag为0表示上一页，1表示下一页
				let arr = changeData(flag,this.blogComments,this.pageComments,this.page,this.maxPageSize,this.commentsLength);
		        this.page = arr[0];
		        this.pageComments = arr[1];
      		},
			submitComment(){
				//提交评论
				console.log(this.comment);
				if(this.comment !== ""){
			        axios({
			              method: 'post',
			              url: '/api/submitComment',
			              data: {
			              	user:window.sessionStorage.user,
			              	comment:this.comment,
			              	blogId:this.blog.id
			              }
			            })
			            .then((response) => {
			            	//console.log(response);
			                if(response['data'][0]['status'] === "200"){
			                	Vue.prototype.$message.success('添加评论成功~');	
			                	this.blogComments = response['data'].slice(1);
			                	this.initPageComments();
			                	this.comment = "";
			                }else{
			                	Vue.prototype.$message.warning('哎呦，评论失败，请待会尝试~')
			                }
			            })
			            .catch((error) => {
			                  
			            })
				}else{
					Vue.prototype.$message.warning('评论内容不能为空~')
				}
				},
				initPageComments(){
					//初始化第一页的评论内容
			        if(this.commentsLength > this.maxPageSize){
			            let start = (this.page - 1) * this.maxPageSize;
			            let end = start + this.maxPageSize;
			            this.pageComments = this.blogComments.slice(start, end); 
			        }else{
			          this.pageComments = this.blogComments;
			        }
			  
				},
				changeState(){
					//当点击收藏时，更换图标的状态
					axios({
			              method: 'post',
			              url: '/api/collectBlog',
			              data: {
			              	user:window.sessionStorage.user,
			              	blogId:this.blog.id
			              }
			            })
			            .then((response) => {
			                if(response['data']['status'] === "200"){
			                	Vue.prototype.$message.success('收藏成功~');
			                	this.ison = 1;
			                }else{
			                	Vue.prototype.$message.warning('哎呦，收藏失败，请待会尝试~')
			                }
			            })
			            .catch((error) => {
			                  Vue.prototype.$message.warning('哎呦，收藏失败，请待会尝试~')
			            })
				},
			lazyload(){
				let imgs = this.$refs.avater;
				if(typeof imgs === "undefined") return;
				const viewHeight = window.innerHeight || document.documentElement.clientHeight
		        for(let i=this.num; i<imgs.length; i++) {
		            // 用可视区域高度减去元素顶部距离可视区域顶部的高度
		            let distance = viewHeight - imgs[i].getBoundingClientRect().top
		            // 如果可视区域高度大于等于元素顶部距离可视区域顶部的高度，说明元素露出
		            if(distance >= 0 ){
		                // 给元素写入真实的src，展示图片
		                imgs[i].src = this.logo;
		                // 前i张图片已经加载完毕，下次从第i+1张开始检查是否露出
		                this.num = i + 1
		            }
		        }
		    }
			},
		created(){
			var that = this;
			//请求博客内容
			axios.get('/api/get_single_blog',{params:{"id":that.id}})
			.then((response)=>{
		          if(response['data'][0]['status'] === "200"){
		          	that.blog = response['data'][1];
		          	that.blog.categories_show = that.blog.category.replace(/-/g,' | '); //由于数据库中存的分类格式是xxx-xxx 因此需要做一些处理用于展示
		          }else{
		          	Vue.prototype.$message.warning("获取数据出错了~~~")
		          }
		    })
		    .catch((response)=>{
		        Vue.prototype.$message.warning("系统发生了异常，请稍后重试~")
		    })
		    //请求评论
		    axios.get('/api/get_comments',{params:{"id":that.id}})
			.then((response)=>{
				  if(response['data'][0]['status'] === "200"){
				  	this.blogComments = response['data'].slice(1);
				  	this.initPageComments();
				  }else{
				  	Vue.prototype.$message.warning(response['data'][0]['msg'])
				  }
		    })
		    .catch((response)=>{
		        Vue.prototype.$message.warning("系统发生了异常，请稍后重试~")
		    })
		},
		mounted(){
			window.addEventListener('scroll', this.lazyload, false);
		},
		updated(){
			this.lazyload();
		},
		  computed:{
		    userName(){
		      return this.$store.state.user; //获取用户名
    		},
    		commentsLength(){
    			return this.blogComments.length;
    		}
  		},
	}
</script>

<style type="text/css" scoped>
@import "../assets/CSS/SingleBlog.css"
</style>
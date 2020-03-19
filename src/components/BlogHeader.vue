<template>
	<div id="header">
		<nav>
			<ul  id='userCenter'> 
				<li> 
					<router-link to='/userCenter' exact>个人中心</router-link>
				</li>
			</ul>
			<ul id="blogHeader">
				<li>
					<router-link to="/" exact>博客首页</router-link> |
	      			<router-link to="/add" exact>添加博客</router-link>
				</li>
			</ul>
			<ul id='login_regist'>
				<li>
					<router-link v-if="isLogin === '0'" to="/login" exact>登录</router-link><span v-if="isLogin === '0'"> | </span>  
					<router-link to="/regist" exact>注册</router-link> 
					<span v-if="isLogin !== '0'"> | <a href="javascript:void(0)" id="logout" @click="logout()">注销</a></span>
				</li>
			</ul>
		</nav>
	</div>
</template>

<script type="text/javascript">
	import Vue from '../main.js'
	export default{
		name:"blogHeader",
		data(){
			return{
			}
		},
		methods:{
			logout(){
				this.$confirm('您确定要注销吗？', '提示', {
          				confirmButtonText: '确定',
          				cancelButtonText: '取消',
          				type: 'warning'
         			}).then(() => {
           			 	this.$store.commit('$_removeStorage');   //注销成功后，移除sessionStorage的用户和登录状态数据
						this.$router.push({'path':'/login'});    //回到登录界面
         			}).catch(() => {
        		});     
			}
		},
		computed:{
			isLogin(){
				console.log(this.$store.state.isLogin);  //判断是否登录了
				return window.sessionStorage.isLogin;
			}
		}
	}
</script>

<style type="text/css" scoped>
	#header{
		overflow: hidden;
		margin-bottom: 40px;
		margin-top: 50px;
	}
	nav{
		width: 1200px;
		background: #428bca;
		height: 60px;
		position: absolute;
		left:50%;
		transform: translate(-50%,-50%);
		padding-top: 20px;
		box-sizing: border-box;
	}

	ul{
		list-style-type: none;
		text-align: center;
		margin:0;
		padding-left: 0;
		display: inline-block;
	}

	li{
		display: inline-block;
	}
	a{
		color:#fff;
		text-decoration: none;
		padding:10px 5px;
		border-radius: 5px;
	}
	.router-link-active{
		background:rgba(255,255,255,0.8);
		color:#444;
	}
	#blogHeader{
		margin-left: 106px;
	}
	#login_regist{
		float: right;
		margin-right: 50px;
	}
	#userCenter{
		float:left;
		margin-left:30px;
	}
</style>
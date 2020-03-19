<template>
    <div>
        <div class="login-wrap">
            <h2>登录</h2>
            <input type="text" placeholder="请输入用户名" v-model="username" required>
            <input type="password" placeholder="请输入密码" v-model="password" required>
            <button @click="login">登录</button>
            <span @click="toRegist()">没有账号？马上注册</span>
        </div>
    </div>
</template>
 
<script>
	import {hex_md5} from '../assets/JS/md5.js'
    import Vue from '../main.js'
    import axios from 'axios'
    export default{
        data(){
            return{
                username: '',
                password: '',
            }
        },
        methods:{
            login(){
            if(this.username === '' || this.password === ''){
                Vue.prototype.$message.warning('请您把信息填写完整~')
                return;
            }
            let md5_password = hex_md5(this.password);
            console.log(md5_password);
            axios({   //把用户名和密码数据发送到后端验证
                  method: 'post',   
                  url: '/api/login',
                  data: {
                    'username':this.username,
                    'password':md5_password
                  },
                })
                .then((response) => {
                      console.log(response);
                      if(response['data']['status'] === "0"){
                        this.$message({
                          message: '登录成功~',
                          type: 'success'
                        })
                        this.$store.commit('$_setStorage', {user: this.username})
                        this.$store.commit('$_setLogin', '1')
                        this.$router.push({name: 'ShowBlogs'})
                      }else{
                       	Vue.prototype.$message.warning(response['data']['msg']);
                      }
                })
                .catch((error) => {
                      Vue.prototype.$message.warning("对不起，发生异常，请稍后再试或联系管理员~");
                })
            },
            toRegist(){
                this.$router.push({'path':'/regist'});
            }
        },
        created(){
            //console.log(this.$store.state.isLogin);
        }
    }
</script>

<style type="text/css" scoped>
    .login-wrap{
        text-align:center;
    }

    input{
        display:block; 
        width:250px; 
        height:40px; 
        line-height:40px; 
        margin:0 auto; 
        margin-bottom: 10px; 
        outline:none; 
        border:1px solid #888; 
        padding:10px; 
        box-sizing:border-box;
    }

    p{
        color:red;
    }

    button{
        display:block; 
        width:250px; 
        height:40px; 
        line-height: 40px; 
        margin:0 auto; 
        border:none; 
        background-color:#41b883; 
        color:#fff; 
        font-size:16px; 
        margin-bottom:5px;
    }

    span{
        cursor:pointer;
    }
    
    span:hover{
        color:#41b883;
    }
</style>

<template>
    <div>
        <div class="register-wrap">
            <h2>注册</h2>
            <input type="text" placeholder="请输入用户名" v-model="newUsername" required>
            <input type="password" placeholder="请输入密码" v-model="newPassword" required>
            <input type="password" placeholder="请再次输入密码" v-model="secondNewPassword" required>
            <button @click="regist()">注册</button>
            <span @click="toLogin()">已有账号？马上登录</span>
        </div>
    </div>
</template>
 
<script>
    import Vue from '../main.js'
    import {hex_md5} from '../assets/JS/md5.js'
    import axios from 'axios'
    export default{
        data(){
            return{
                newUsername: '',
                newPassword: '',
                secondNewPassword:'',
            }
        },
        methods:{
            regist(){
            if(this.newUsername === '' || this.newPassword === '' || this.secondNewPassword === ''){
                Vue.prototype.$message.warning('请您把信息填写完整~');
                return;
            }
            if(this.newPassword !== this.secondNewPassword){
                Vue.prototype.$message.warning('两次输入的密码不一致，请重新填写~');
            }
            let md5_password = hex_md5(this.newPassword);
            axios({ //提交数据到后端注册账号
                  method: 'post',
                  url: '/api/regist',
                  data: {
                    'newUsername':this.newUsername,
                    'newPassword':md5_password,
                  },
                })
                .then((response) => {
                      console.log(response);
                      if(response['data']['status'] === "0"){
                        this.$message({
                          message: response['data']['msg'],
                          type: 'success'
                        })
                        this.$router.push({'path':'/login'});
                      }else{
                        this.$message.error(response['data']['msg']);
                      }
                })
                .catch((error) => {
                      Vue.prototype.$message.warning("对不起，发生异常，请稍后再试或联系管理员~");
                })

            },
            toLogin(){
                 this.$router.push({'path':'/login'});
            }
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

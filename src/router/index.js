import Vue from 'vue'
import VueRouter from 'vue-router'

//注册插件
Vue.use(VueRouter)

const routes = [
  {
    path: '/', 
    name: 'ShowBlogs',
    component: () => import('../components/ShowBlogs.vue')
  },
  {
    path: '/add',
    name: 'AddBlog',
    meta: {auth: true},
    component: () => import('../components/AddBlog.vue')
  },
  {
    path:'/blog/:id/:canDelete',
    name:'SingleBlog',
    meta: {auth: true},
    component:() => import('../components/SingleBlog.vue')
  },
  {
    path:'/edit-blog/:id',
    name:'EditBlog',
    meta: {auth: true},
    component:() => import('../components/EditBlog.vue')
  },
  {
    path:'/login',
    name:"login",
    component:() => import('../components/Login.vue')
  },
  {
    path:'/regist',
    name:"regist",
    component:() => import('../components/Regist.vue')
  },
  {
    path:'/userCenter',
    name:'userCenter',
    meta: {auth: true},
    component:() => import('../components/UserCenter.vue')
  },
  {
    path:'/clock',
    name:'clock',
    component:() => import('../components/clock.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

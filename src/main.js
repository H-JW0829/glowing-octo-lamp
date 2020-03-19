import Vue from 'vue'
import App from './App.vue'
import $ from 'jquery'
import router from './router'
import store from './store'
import VueResource from 'vue-resource'
import axios from 'axios'
import { Message } from 'element-ui'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css'
Vue.prototype.$http=axios
Vue.config.productionTip = false
Vue.use(VueResource)
Vue.prototype.$message = Message
Vue.use(ElementUI);
//自定义指令
Vue.directive('rainbow',{
	bind(el,bingding,vnode){
		el.style.color = "#" + Math.random().toString(16).slice(2,8);
	}
})

//过滤器
Vue.filter("toUpper",function(value){
	return value.toUpperCase();
})


Vue.filter("lessSentences",function(value){
	return value.slice(0,100) + "....";
})

//全局的路由钩子函数 next(false)不跳转
router.beforeEach((to, from, next) => {
  if (to.matched.some(m => m.meta.auth)) {
    if (window.sessionStorage.isLogin === '1') {
      next()
    } else if (to.path !== '/login') {
      next({path: '/login'}) //跳转到登录页面
      Vue.prototype.$message.warning('检测到您还未登录,请登录后操作~')
    }
  } else {
    next()
  }
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

export default Vue

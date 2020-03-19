import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
import axios from 'axios'
const key = 'user'
const isLogin = 'isLogin'
export default new Vuex.Store({
  state: {
  	  user: null,
      isLogin: '0',
      authors : [],
  },
  mutations: {
  	$_setLogin (state, value) {
      state.isLogin = value
      sessionStorage.setItem(isLogin, value)
    },
    $_setStorage (state, value) {
      state.user = value
      sessionStorage.setItem(key, JSON.stringify(value))
    },
    $_removeStorage (state) {
      state.user = null
      state.isLogin = '0'
      sessionStorage.removeItem(key)
      sessionStorage.setItem(isLogin, '0')
    },
    setAuthors(state,authors){
    	state.authors = [];
    	for(let author of authors){
    		state.authors.push(author['user_name']);
    	}
    }
  },
  actions: {
  	getAuthors(context){
  		axios({
            method: 'post',
            url: '/api/get_authors',
          })
          .then((response) => {
               if(response['data'][0]['status'] === '200'){
               		let data = response['data'].slice(1);
               		context.commit('setAuthors', data) ;
               }else{
               		return;
               }
          })
          .catch((error) => {
                alert("对不起，发生异常，请稍后再试或联系管理员~");
          })
  	}
  },
  getters:{
  	 getStorage: function (state) {
      if (!state.user) {
        state.user = JSON.parse(sessionStorage.getItem(key))
        state.isLogin = sessionStorage.getItem(isLogin)
      }
      return state.user
    }
  }
})

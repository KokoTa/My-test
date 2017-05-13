import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

const state = { // 状态对象， 存放公共数据
	count: 4
}

const mutations = { // 状态方法， 改变数据的方法
	increase (state) {
		state.count++
	},
	decrease (state) {
		state.count--
	}
}

export default new Vuex.Store({
	state,
	mutations
})
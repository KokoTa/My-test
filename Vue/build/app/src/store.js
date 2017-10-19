import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

const state = { // 状态对象， 存放公共数据
	count: 4
}

const mutations = { // 触发状态， 注意方法都是同步的
	increase (state, n) {
		state.count += n.a
	},
	decrease (state) {
		state.count--
	}
}

const getters = { // 计算状态， 不改变状态对象， PS：computed不要用箭头函数， this会出错
	count: function (state) {
		return state.count + 100
	}
}

const actions = {
	add (context) { // context等于整个sotre
		context.commit('increase', {a:100}) // 提交触发mutations中的方法
		setTimeout(() => { // 模仿异步调用
			context.commit('decrease')
		}, 3000)
		console.log('我能继续执行')
	},
	del ({commit}) { // 结构赋值简化代码
		commit('decrease')
	}
}

// const moduleA = { // 集合成模块A
// 	state,
// 	mutations,
// 	getters,
// 	actions
// }

//输出实例， 被组件使用
export default new Vuex.Store({
	// modules: {
	// 	a:moduleA
	// }
	state,
	mutations,
	getters,
	actions
})
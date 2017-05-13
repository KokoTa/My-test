import Vue from 'vue'
import store from './store'
import vuex from './vuex.vue'

new Vue({
	el: '#app',
	store,
	render: x => x(vuex)
})
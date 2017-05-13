<template>
	<div id="app">
		<h1>Hello</h1>
		<p>{{ count }} - {{ count2 }} - {{ count3 }}</p>
		<button @click='$store.commit("increase")'>+</button>
		<button @click='$store.commit("decrease")'>-</button>
	</div>
</template>

<script>
	import { mapState } from 'vuex'
	export default {
		data () {
			return {
				num: 1
			}
		},
		// computed: {
		// 	count () {
		// 		return this.$store.state.count + 1 // 一直这样引入太麻烦，引入mapState简化操作
		// 	}
		// }
		computed: mapState({
			count: state => state.count, // 写法一
			count2: 'count', // 写法二， 'count' 等同于 `state => state.count`
			count3 (state) { // 写法三， 当需要运用到局部状态时需使用常规函数
				return state.count + this.num
			}
		})
	}
</script>
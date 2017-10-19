<template>
	<div id="app">
		<h1>Hello</h1>
		<p>{{ count }}</p>
		<button @click='increase({ a: 10 })'>+</button>
		<button @click='decrease'>-</button>
		<button @click='add'>add</button>
		<button @click='del'>del</button>
	</div>
</template>

<script>
	import { mapState, mapGetters, mapMutations, mapActions } from 'vuex'
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
		// mapState映射状态， mapGetters映射派生状态， mapMutations映射方法， 其中前两个不改变状态对象, mapActions进行异步操作后触发mapMutations
		// 写法一
		// 写法二， 'count' 等同于 `state => state.count`
		// 写法三， 当需要运用到局部状态时需使用常规函数
		// ...{} 混入
		// computed: {
		// 	...mapState({
		// 		count: state => state.count, 
		// 		count2: 'count', 
		// 		count3 (state) { 
		// 			return state.count + this.num
		// 		}
		// 	}),
		// 	...mapGetters({
		// 		count4: 'count'
		// 	})
		// },
		computed: {
			...mapState(['count'])
		},
		methods: {
			...mapMutations([ // 映射方法, 注意这个是数组， 当然也可以用对象形式写
				'increase',
				'decrease'
			]),
			...mapActions([
				'add','del'
			])
		}
	}
</script>
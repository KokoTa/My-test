import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter)

const FIRST = {
	template: `<div>
	   <h1>First Template</h1>
	   <p>{{ $route.query.x }}</p>
	   <!--注意：子模板里无法用JSON.stringify格式化$route-->
	</div>`
}
const SECOND = {
	template: `<div>
	   <h1>Second Template</h1>
	</div>`
}
const HOME = {
	template: `
		<div>
			<h1>Home Template</h1>
			<router-view></router-view>
		</div>
	`
}
const urlParam = {
	template: `
		<div>
			{{ $route.params.user }} | {{ $route.params.id }}
		</div>
	`
}
const ERROR = {
	template: `
		<h1>Error Page</h1>
	`
}

const router = new VueRouter({
	mode: 'history', // 模式
	base: __dirname, // 根路径, 其实就是/
	routes: [ // 路由配置
		{
			path: '/', 
			component: HOME, // 父模板
			name: 'Home',
			children: [
				{ path: 'children', name: 'Home-child', component: FIRST } // 子模版
			]
		},
		{ path: '/first', name: 'First', component: FIRST}, // 单模板
		{ path: '/second', name: 'Second', components: { default: SECOND, a: FIRST, b: FIRST}}, // 多模板输出
		{ path: '/url/:user/:id(\\d+)', name: 'url', component: urlParam}, // 正则限制注意转义
		{ path: '*', component: ERROR, 
			beforeEnter: (to, from, next) => { 
				console.log(to);
				console.log(from);
				next({ path: '/' }) // next()表示可以执行下一步， next(false)拒绝执行下一步， next(path: 'xxx')导向其他路由
			} 
		} // 针对不存在的路由, 要放在最后一个
	]
})

// $route的对象指向最里层的模板对象	
new Vue({
	router, // 加载路由
	template: `
		<div id='demo'>
			<button @click='goBack'>后退</button>
			<button @click='goTo'>前进</button>
			<p>--------------------------------------</p>
			<ul>
				<li><router-link to='/'>AAA</router-link></li><!--尝试添加exact看看效果-->
				<li><router-link to='/first'>BBB</router-link></li>
				<li><router-link :to="{ name: 'Second'}">CCC</router-link></li>
				<li><router-link :to="{ path: '/children', query: { x: 666 }}">DDD</router-link></li> <!--path加/是绝对路径, 不加就等于是在当前url后再追加; name一定要和params配合使用， path将导致params无效-->
				<li><router-link :to="{ path: '/url/KokoTa/123123' }">EEE</router-link></li>
			</ul>
			<router-view></router-view>
			<router-view name='a'></router-view>
			<router-view name='b'></router-view>
			<p>--------------------------------------</p>
			<p>Template Name: {{ $route.name }}</p>
		</div>
	`,
	methods: {
		goBack () {
			router.go(-1)
		},
		goTo () {
			router.go(1)
		}
	}
}).$mount('#app') // 发布
var path = require('path')
var HTMLwebpackPlugin = require('html-webpack-plugin')
var UglifyJSPlugin = require('uglifyjs-webpack-plugin')
var webpack = require('webpack')
// var ExtractTextPlugin = require('extract-text-webpack-plugin')

// 定义路径
var ROOT = path.resolve(__dirname)
var APP = path.resolve(__dirname, 'app')
var BUILD = path.resolve(__dirname, 'build')
var TEMP = path.resolve(__dirname, './app/templates')

module.exports = {
	//项目的文件夹 可以直接用文件夹名称 默认会找index.js 也可以确定是哪个文件名字
	entry: {
		// 三个入口文件
		// 打包成app.js
		app: path.resolve(APP, 'index.js'),
		mobile: path.resolve(APP, 'app.js'),
		// 添加要打包的库， 分离第三方库
		vendors: ['jquery', 'moment']
	},
	//输出的文件名 合并以后的js会命名为bundle.js
	output: {
		path: BUILD,
		//注意 我们修改了bundle.js 用一个数组[name]来代替，他会根据entry的入口文件名称生成多个js文件，这里就是(app.js,mobile.js和vendors.js)
		filename: '[name].js',
		publicPath: 'http://localhost:8080/public/' // 公共资源目录， eg:http://localhost:8080/public/index.html
	},
	//添加我们的插件 会自动生成一个html文件
	plugins: [
		// 自动生成页面
		new HTMLwebpackPlugin({ 
			title: 'A page',
			template: path.resolve(TEMP, 'index.html'),
			filename: 'index.html',
			chunks: ['app', 'vendors'], // 要引用entry里面的哪几个入口
			inject: 'body' // 把script插入到标签里
		}),
		new HTMLwebpackPlugin({
			title: 'B page',
			template: path.resolve(TEMP, 'mobile.html'),
			filename: 'mobile.html',
			chunks: ['mobile', 'vendors'], // 要引用entry里面的哪几个入口
			inject: 'body' // 把script插入到标签里
		}),
		// 输出第三方库
		new webpack.optimize.CommonsChunkPlugin({
			name: 'vendors',
			filename: 'vendors.js'
		}),
		// new ExtractTextPlugin('./extract/extract.css'),
		// 压缩代码, 有大坑= =, 作者也表示V3版本不兼容某些功能
		new UglifyJSPlugin({
			compress: true
		})
	],
	module: {
		rules: [ // 加载器使用及设置
			// {
			// 	test: /\.scss$/, // 编译后单独提取CSS
			// 	use: ExtractTextPlugin.extract({
			// 		use: 'css-loader!sass-loader'
			// 	})
			// },
			{
				test: /\.scss$/, // 编译后插入到HTML中, 图片引用会被下下一个loader继续处理
				loader: 'style-loader!css-loader?sourceMap!sass-loader?sourceMap',
				include: APP // 只包含APP路径下的文件
			},
			{
				test: /\.html$/, // 编译HTML， 图片引用会被下一个loader继续处理
				loader: 'html-loader'
			},
			{
				test: /\.(jpg|png)$/,
				loader: 'url-loader?limit=40000&name=imgs/[hash:8].[name].[ext]' // 小于40000的文件都会编辑为base64格式
			},
			{
				test: /\.jsx?$/, // js或jsx文件
				loader: 'babel-loader',
				include: APP,
				query: {
					presets: ['es2015'] // es2015这个参数是babel的plugin，可以支持各种最新的es6的特性
				}
			}
		]
	},
	devtool: 'eval-source-map', // 采用source-map形式显示错误代码位置
	// 服务器配置
	devServer: { 
		// hot: true, // 热更新, 默认true
		// inline: true, // 重载脚本注入的bundle.js, 默认true
		proxy: { // 路由代理
			'/api/*': { // api/*的请求都代理到localhost
				target: 'http://localhost:8080',
				secure: false // 是否运行再https上
			}
		}
	}
	// watch: true, // 是否自动打包
	// externals: { ...: 'www.xxx.xx.js' } // 引入CDN外部库
}
// webpack配置文件

const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin'); // 利用模板index.tmpl.html生成index.html，会自动添加所依赖的 css, js，favicon等文件
const ExtractTextPlugin = require('extract-text-webpack-plugin'); // 分离CSS和JS文件

module.exports = {
	devtool: "source-map", // 提供了编译文件和源文件对应的方法
	entry: __dirname + "/app/main.js", // 加载入口
	output: {
		path: __dirname + "/build", // 输出出口
		filename: 'bundle-[hash].js' // 打包后输出的文件名，随机生成的hash利于缓存
	},
	devServer: { // webpack-dev-server：热加载服务器插件
	  contentBase: "./build",// 加载的资源路径
	  historyApiFallback: true, // 用于开发单页应用，所有跳转都指向index.html，即不跳转
	  inline: true, // 开启实时刷新
	  hot: true // 模块热加载HMR
	},
	module: { // 配置loader
	  rules: [
      {
        test: /(\.jsx|\.js)$/,
        use: {
          loader: "babel-loader",
          // 由于有很多配置项，所以可以把这些配置单独拿出来
          // 放到.bablrc中，webpack会自动调用这个文件
          // options: {
          //   presets: [
          //     "es2015", "react"
          //   ]
          // }
        },
        exclude: /node_modules/ // 屏蔽的文件
      },
      {
        test: /\.css$/,
        // 未使用ExtractTextPlugin
        // use: [
        // 	{
	       //    loader: "style-loader" // 将所有的计算后的样式加入页面中
	       //  }, 
	       //  {
	       //  	loader: "css-loader", // 使用类似@import和url(...)的方法实现require()的功能
	       //  	options: {
	       //  		modules: true, // 开启CSS模块化
	       //  		importLoaders: 1
	       //  	}
	       //  },
	       //  {
	       //  	loader: "postcss-loader"
	       //  }
        // ],
        // 使用ExtractTextPlugin
        use: ExtractTextPlugin.extract({
          fallback: "style-loader",
          use: [{
            loader: "css-loader",
            options: {
              modules: true
            }
          }, {
            loader: "postcss-loader"
          }],
	      }),
        exclude: /node_modules/ // 屏蔽的文件
      }
	  ]
  },
  plugins: [ // 配置插件
  	new webpack.BannerPlugin("Created by KokoTa"), // 版权声明插件
  	new HtmlWebpackPlugin({
      template: __dirname + "/app/index.tmpl.html" // 指定模板
    }),
    new webpack.HotModuleReplacementPlugin(), // 热加载HMR插件，React需配合babel的react-transform-hrm使用
    new webpack.optimize.OccurrenceOrderPlugin(), // 为组件分配ID，webpack自带
    new webpack.optimize.UglifyJsPlugin(), // 压缩JS代码，webpack自带
    new ExtractTextPlugin("style.css") // 分离CSS和JS文件，需安装extract-text-webpack-plugin
  ]
}
// 入口文件
// 使用babel后替换commonjs风格
// require('./main.scss')
// var sub = require('./sub') // 引用module
// var app = document.createElement('div')
// var $ = require('jquery')
// var moment = require('moment')

// app.innerHTML = 'Hello KokoTa'
// app.appendChild(sub())
// document.body.appendChild(app)

// $('body').append('<h2>Now is ' + moment().format() + '</h2>')

import './main.scss'
import generateText from './sub.js'
import $ from 'jquery'
import moment from 'moment'
// 注意这种写法, 把jQuery这个变量直接插入到plugin.js里面了
// 相当于在这个文件的开始添加了 var jQuery = require('jquery');
import 'imports-loader?jQuery=jquery!./plugin.js'

let app = document.createElement('div')
const myPromise = Promise.resolve(42)
myPromise.then((number) => {
	$('body').append('<h1>Promise result is ' + number + ' now is ' + moment().format() + '</h1>')
	// 可以正常使用 jquery plugin 了
	$('h1').greenify()
})
app.innerHTML = '<h1>Hello Webpack</h1>'
document.body.appendChild(app)
app.appendChild(generateText())
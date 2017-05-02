var http = require('http') // 网络通信模块
var fs = require('fs') // 文件操作模块
var url = require('url') // url解析
var util = require('util') // 实用工具

http.createServer(function (req, res) {
	var path = 'F:/Github/Program/My-test/Node/Node入门(watch video about wos)/GET' // 文件绝对路径常量
	var pagePath = url.parse(req.url).pathname // 解析文件名, ...:3000/page1.html -> page1.html

	res.writeHead(200, {'Content-Type': 'text/html'}) // 响应类型
	if (url.parse(req.url).pathname != '/favicon.ico') { // 跳过强制的小图标读取
		var data = fs.readFileSync(path + pagePath, 'utf-8') // 同步读取文件
		res.write(data)
	}
	
	res.write(util.inspect(url.parse(req.url))) // util.inspect使无法读取的对象标准化后可读取

	res.end() // 响应结束
}).listen(3000)

console.log('Listening...')
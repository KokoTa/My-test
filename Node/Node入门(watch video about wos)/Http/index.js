// 模仿客户端发送请求和接受响应
// 先打开GET文件夹内的服务器

var http = require('http')

var options = { // 请求头
	hostname: 'localhost',
	port: 3000,
	path: '/page1.html',
	method: 'GET'
}

var req = http.request(options, function (res) {
	console.log(res.statusCode) // 状态码
	console.log(res.headers) // 头信息

	res.on('data', function (chunk) { // 返回的所有数据
		console.log(chunk.toString())
	})

})

req.on('error', function (e) {
	console.log(e.message)
})

req.end()
var http = require('http'),
	fs = require('fs'),
	url = require('url'),
	querystring = require('querystring'), // 解析查询键值对
	formidable = require('formidable') // 第三方组件： 文件上传

var server = http.createServer(function (req, res) {
	var pathname = url.parse(req.url).pathname
	if (pathname == '/index') { // 读取主页
		var pageContent = fs.readFile('index.html', 'utf-8', function (err, data) {
			if (err) {
				res.end('Server.error: 101' + err)
			}
			res.writeHead(200, {'Content-Type': 'text/html'})
			// res.write(data)
			res.end(data)
		})
	} else if (pathname == '/post') { // 上传数据
		var post = ''
		req.on('data', function (chunk) { // 数据片段拼接
			post += chunk
		})
		req.on('end', function () {
			post = querystring.parse(post) // 解析表单
			res.writeHead(200, {'Content-Type': 'text/plain'})
			res.write(post.name + ', ' + post.email + ', ' + post.address)
			res.end()
		})
	} else if (pathname == '/postFile') { // 上传文件
		var form = new formidable.IncomingForm() // 创建新的传输表单
		form.uploadDir = './temp' // 服务器临时空间, 存放临时文件
		form.parse(req, function(err, fields, files) { // 格式化文件
			// console.log(files)
			var path = files.file.path // 获得临时空间的文件， file为表单名
			fs.rename(path, './temp/1.jpg') // 将临时文件转为指定格式的文件（设置文件名并输出）
			res.end()
		})
	} else { // 错误处理
		res.writeHead(404, {'Content-Type': 'text/plain'})
		res.end('Error')
	}
}).listen(3000)

console.log('Listening at port 3000...')
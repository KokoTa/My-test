// 方便建立websocket的模块

var io = require('socket.io')
var socket = io.listen('3000') // 建立服务器(端口，IP)

socket.on('connection', function (client) { // 客户端文件的socket插件与服务器建立链接后
	console.log('客户端连接到服务器啦.')
	client.send('Hello World') // 发送信息
	client.emit('news', 'Gretting') // 自定义指令数据，传给客户端
	client.on('cute', function (data) { // 接收客户端数据
		console.log(data)
	})
})
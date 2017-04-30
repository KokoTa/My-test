// net 模块练习， 聊天室
// http模块继承了Net类，做了更多的数据封装
// net模块一般用于开发即时通讯。
// 用node、telnet进行测试

var net = require('net') // 引入net模块
var chatServer = net.createServer() // 建立服务器
var clientList = [] // 用户数组

chatServer.on('connection', function (client) { // 连接客户端
	client.write('Hello World...\n\r') // 客户端输出, \r处理windows回车bug
	// client.end() // 结束连接

	client.name = client.remoteAddress + ':' + client.remotePort // 添加name属性，IP+Port
	clientList.push(client) // 添加用户
	console.log(client.name + ' joind\n\r')

	client.on('data', function(data) { // 监听数据变动
		for(var i = 0 ; i < clientList.length ; i++) {
			if (client != clientList[i]) {
				clientList[i].write(client.name + ':' + data.toString() + '\n\r') // 向其他客户端输出数据
			}
		}
	})

	client.on('end', function () {
		clientList.splice(clientList.indexOf(client), 1) // 删除用户
	})
	
	client.on('error', function (e) {
		console.log(e)
	})
}).listen(3000)
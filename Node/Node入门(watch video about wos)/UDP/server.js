// TCP安全不丢包速度慢， UDP不安全会丢包速度快， TCP一对一， UDP一对多
// UDP可结合aflax使用

var dgram = require('dgram') // dgram: 数据包
var server = dgram.createSocket('udp4') // 创建实例

server.on('error', function (err) {
	console.log(err.stack)
	server.close()
})

server.on('message', function (msg, info) {
	console.log(msg) // 客户端发送的信息
	console.log(info.address) // 客户端地址
	console.log(info.port) // 客户端端口号
})

server.on('listening', function () {
	var address = server.address()
	console.log(address.address) // 服务器地址
	console.log(address.port) // 服务器端口
})

server.bind('3000')
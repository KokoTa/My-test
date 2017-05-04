var dgram = require('dgram')
var msg = new Buffer('Greeting') // 发送报文用Buffer
var client = dgram.createSocket('udp4') // 创建实例, 格式有udp4/udp6, 服务器和客户端要对应
// 0:代表使用Buffer模式, msg.length报文长度减少错误可能性, 端口号， 地址， 处理函数
client.send(msg, 0, msg.length, 3000, 'localhost', function (err, byte) {
	client.close()
}) 
var net = require('net');
var client = net.connect({port: 3000}, function() { // 连接服务器
   console.log('连接到服务器！');  
});
client.on('data', function(data) { // 接收服务器数据
   console.log(data.toString());
   client.end();
});
client.on('end', function() { // 断开连接
   console.log('断开与服务器的连接');
});